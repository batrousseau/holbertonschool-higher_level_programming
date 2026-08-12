#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute


class MyClass():
    pass
mc = MyClass()
add_attribute(mc, "hbtn", "Holberton")
print(mc.hbtn)