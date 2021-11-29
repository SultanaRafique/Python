def grade(num):
    if num >= 90.0:
        print("A")
    elif num >= 80.0:
        print("B")
    elif num >= 70.0:
        print("C")
    elif num >= 60.0:
        print("D")
    else:
        print("F")


usr_input = float(input("enter numbers: "))
grade(usr_input)

