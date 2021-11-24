import math as m
import functools, sqlite3
from math import pi
from os import mkdir, rmdir
from math import *
from sys import *

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def test():
    for i in range(10):
        print("hello", i)
        # print(10/0)


def compute_area():
    radius = 20.0
    area = radius * radius * 3.14
    print(area)
    print("The area for the circle of radius {} is {}".format(radius, area))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
    print("hello world")
    test()
    compute_area()
    my_value = input("enter you age: ").strip()
    print(type(my_value))
    my_val = int(my_value)

    print(type(my_val))
    print("your age is {} ".format(my_value))
    print("your age is {} {} {}".format(my_value, 20, "ok!"))
    print("your age is {2} {0} {1}".format(my_value, 20, "ok!"))

    print("your age is", my_value)
    print("my age is " + my_value)

    s = "hello"
    print(s[2:5])
    print(s[0:5])
    print(s.capitalize())
    print(len(s))

    my_value = input("enter you name: ").strip()
    my_value = my_value.split(' ')
    print(my_value)
    print(my_value[1])

    print("http://perscholas.org".replace('http', 'https'))

    print(1.0 - 0.9)
    print(chr(97))
    print(ord('S'))


def convert_sec(time_in_sec):
    minute = int(time_in_sec / 60)
    sec = time_in_sec % 60
    time = "{} minutes and {} seconds {}".format(minute, sec)
    return time
