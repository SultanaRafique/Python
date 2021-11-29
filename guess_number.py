import random


def guess_num():
    rand = random.randint(0, 6)
    uer_input = int(input("Enter number: "))

    while rand != uer_input:
        if uer_input < rand:
            print("Number is too low")
            uer_input = int(input("Sorry! try again: "))
        elif uer_input > rand:
            print("Number is too high")
            uer_input = int(input("Sorry! try again: "))

    if rand == uer_input:
        print("your guess is correct")
        return


guess_num()
