from serializers.json_serializer import JsonSerializer
from serializers.xml_serializer import XMLSerializer


class SerializerFactory:

    @staticmethod
    def create_serializer(format_type: str):

        match format_type.lower():

            case "json":
                return JsonSerializer()

            case "xml":
                return XMLSerializer()

            case _:
                raise ValueError

            