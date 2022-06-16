print("Welcome to *title*")
loop = 1
route = 0
optionloop = 0
paraloop = 1

def paragraph(route):
    if route == 1:
        print("paragraph 1")
        route = optionpick(1, route, 0)
        return route
    elif route == 2:
        print("paragraph 2")
        route = optionpick(1, route, 0)
        return route
    elif route == 11:
        print("paragraph 11")
    elif route == 22:
        print("paragraph 22")
    elif route % 3 == 0:
        print("paragraph 12/21")
        return route


def optionpick(option, route, optionLoop):
    option = int(input("Do you pick option 1 or 2?\n>> "))
    optionloop = 1
    while optionloop == 1:
        if option == 1 or option == 2:
            optionloop = 0
            return ((route*10)+option)
        else:
            option = int(input("Please only pick option 1 or 2, now try again.\n>> "))
    return route

while loop == 1:
    start=input("Are you ready to start?\ntype yes to start\n>> ")
    start=start.lower()
    while start == "yes":
        start = "no"
        loop -= 1
        print("\n*entry paragraph*")
        route = optionpick(1, 0, 0)
        route = paragraph(route)
        paragraph(route)

        print("\n \n \n ")
        start = input('Do you want to try again and achieve all three endings?\ntype yes to start\n>> ')
        start = start.lower()
    else:
        print("If you meant to start then please type yes exactly, otherwise goodbye.\n \n")
