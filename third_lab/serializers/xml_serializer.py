import regex

from utilities.serializer_utilities import serialize
from utilities.deserializer_utilities import deserialize
from constants.xml_serializer_constants import *


class XMLSerializer:

    def dumps(self, obj):
        return self.convert(serialize(obj))

    def dump(self, obj, file):
        file.write(self.dumps(obj))

    def loads(self, string):
        return deserialize(self.find(string))

    def load(self, file):
        return self.loads(file.read())

    def convert(self, value):

        if isinstance(value, (int, float, bool)):
            return f"<{type(value).__name__}>{str(value)}</{type(value).__name__}>"

        elif isinstance(value, str):
            value = value.replace('"', "&quot;").replace("'", "&apos;").replace("<", "&lt;").replace(">", "&gt;")\
                         .replace("&", "&amp;")
            return f"<str>{value}</str>"

        elif isinstance(value, list):
            value = "".join([self.convert(val) for val in value])
            return f"<list>{value}</list>"

        elif isinstance(value, dict):
            value = "".join([f"{self.convert(key)}{self.convert(val)}" for key, val in value.items()])
            return f"<dict>{value}</dict>"

        elif not value:
            return "<NoneType>None</NoneType>"

    def find(self, string):

        result = regex.fullmatch(ELEMENT, string)

        if not result:
            return

        key = result.group("key")
        value = result.group("value")

        match key:

            case "int":
                return int(value)

            case "float":
                return float(value)

            case "bool":
                return str(value) == "True"

            case "NoneType":
                return None

            case "str":
                return value.replace("&quot;", '"').replace("&apos;", "'").replace("&lt;", "<").replace("&gt;", ">")\
                            .replace("&", "&amp;")

            case "list":
                result = regex.findall(ELEMENT, value)
                return [self.find(match[0]) for match in result]

            case "dict":
                result = regex.findall(ELEMENT, value)
                return {self.find(result[i][0]): self.find(result[i + 1][0]) for i in range(0, len(result), 2)}
