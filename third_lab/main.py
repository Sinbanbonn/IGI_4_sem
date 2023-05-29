from serializers.serializer_factory import SerializerFactory
from prettytable import PrettyTable


class A:

    a = 99

    def __init__(self):
        self.b = 9.9

    def test_method_1(self):
        return self.a / self.b

    @staticmethod
    def static_method_1():
        return "static success!"


class B(A):

    def test_method_2(self):
        return self.a + self.b


if __name__ == '__main__':

    json_serializer = SerializerFactory.create_serializer("JSON")
    xml_serializer = SerializerFactory.create_serializer("XML")

    default_object = B()

    with open("results/result.json", "w") as f:
        json_serializer.dump(default_object, f)

    with open("results/result.xml", "w") as f:
        xml_serializer.dump(default_object, f)

    json_obj_dumps = json_serializer.dumps(default_object)
    xml_obj_dumps = xml_serializer.dumps(default_object)

    json_object = json_serializer.loads(json_obj_dumps)
    xml_object = xml_serializer.loads(xml_obj_dumps)

    json_class_dumps = json_serializer.dumps(B)
    xml_class_dumps = xml_serializer.dumps(B)

    json_class = json_serializer.loads(json_class_dumps)
    xml_class = xml_serializer.loads(xml_class_dumps)

    table = PrettyTable(["INFO", "default", "JSON", "XML"])
    table.add_row(["field a", default_object.a, json_object.a, xml_object.a])
    table.add_row(["field b", default_object.b, json_object.b, xml_object.b])
    table.add_row(["method 1", default_object.test_method_1(), json_object.test_method_1(), xml_object.test_method_1()])
    table.add_row(["method 2", default_object.test_method_2(), json_object.test_method_2(), xml_object.test_method_2()])
    table.add_row(["static method", B.static_method_1(), json_class.static_method_1(), xml_class.static_method_1()])

    print(table)
