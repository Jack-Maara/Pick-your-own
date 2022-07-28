import paragraphdef
import optionpick

print("Welcome to your new mailbox\n")
loop = 1
route = 0
optionloop = 0
paraloop = 1
def readfile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} not found")
while loop == 1:
    start = input("Are you ready to start?\ntype yes to start\n>> ")
    start = start.lower()
    while start == "yes":
        start = "no"
        loop -= 1
        readfile("intro.txt")
        route = optionpick.optionpick(1, 0, 0)
        route = paragraphdef.paragraph(route)
        paragraphdef.paragraph(route)
        print("\n \n \n ")
        start = input('Do you want to try again and achieve all three endings?\n\ntype yes to start\n>> ')
        start = start.lower()
        loop = 1
    else:
        print("If you meant to start then please type yes exactly, otherwise goodbye.\n \n")
