from optionpick import *


def readfile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} not found")


def paragraph(route):
    if route == 1:
        readfile("para1.txt")
        route = optionpick(1, route, 0)
        return route
    elif route == 2:
        readfile("para2.txt")
        route = optionpick(1, route, 0)
        return route
    elif route == 11:
        readfile("para11.txt")
    elif route == 22:
        readfile("para22.txt")
    elif route % 3 == 0:
        readfile("para121.txt")
        return route
