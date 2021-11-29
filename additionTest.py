import random


def add_test():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    res = num1 + num2
    user_res = int(input(" {} + {} = ".format(num1, num2)))
    if user_res == res:
        print("True")
    else:
        print("False")


add_test()

