def optionpick(option, route, optionLoop):
    option = int(input("Do you pick option 1 or 2?\n>> "))
    optionloop = 1
    while optionloop == 1:
        if option == 1 or option == 2:
            optionloop = 0
            return route * 10 + option
        else:
            option = int(input("Please only pick option 1 or 2, now try again.\n>> "))
    return route