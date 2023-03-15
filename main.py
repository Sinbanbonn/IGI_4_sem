import time

print("Hello World!")
while True:
    i = 5
    time.sleep(40)
#“add”, “sub”, “mult” and “div”
def calculator(x , y , operation):
    if operation == "add" :
        return x + y
    elif operation == "sub" :
        return x - y
    elif operation == "mult":
        return x * y
    elif operation == "div":
        return x/y
