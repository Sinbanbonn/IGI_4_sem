from custom_serializer import SerializerFactory

if __name__ == '__main__':
    xml = SerializerFactory.serializer('xml')
    with open('test.xml', 'w') as file:
        xml.dump([1,2,3], file)
    ser = xml.dumps([1, 2, 3, 4, 5])
    print(ser)
    des = xml.loads(ser)
    print(des)
