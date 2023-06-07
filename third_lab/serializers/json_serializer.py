from utilities.serializer_utilities import serialize
from utilities.deserializer_utilities import deserialize
from constants.json_serializer_constants import *
import regex


class JsonSerializer:

    def dumps(self, obj):
        return self.convert(serialize(obj))

    def dump(self, obj, file):
        file.write(self.dumps(obj))

    def loads(self, string):
        return deserialize(self.find(string))

    def load(self, file):
        return self.loads(file.read())

    def convert(self, value):

        if isinstance(value, str):
            return '"' + value.replace("\\", "\\\\").replace('"', "\"").replace("'", "\'") + '"'

        elif isinstance(value, (int, float, complex, bool)):
            return str(value).lower()

        elif isinstance(value, dict):
            return "{" + ", ".join([f"{self.convert(key)}:{self.convert(value)}" for key, value in value.items()]) + "}"

        elif isinstance(value, list):
            return "[" + ", ".join([self.convert(val) for val in value]) + "]"

    def find(self, string):

        string = string.strip()

        result = regex.fullmatch(INT, string)
        if result:
            return int(result.group(0))

        result = regex.fullmatch(FLOAT, string)
        if result:
            return float(result.group(0))

        result = regex.fullmatch(BOOL, string)
        if result:
            return result.group(0) == "true"

        result = regex.fullmatch(NONE, string)
        if result:
            return None

        result = regex.fullmatch(STR, string)
        if result:
            res = result.group(0)
            res = res.replace("\\\\", "\\").replace(r"\"", '"').replace(r"\'", "'")
            return res[1:-1]

        if string[0] == "[" and string[-1] == "]":
            string = string[1:-1]
            result = regex.findall(VALUE, string)
            return [self.find(match[0]) for match in result]

        if string[0] == "{" and string[-1] == "}":
            string = string[1:-1]
            result = regex.findall(VALUE, string)
            return {self.find(result[i][0]): self.find(result[i + 1][0]) for i in range(0, len(result), 2)}
