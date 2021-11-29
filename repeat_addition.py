from random import random

import random


def repeat_add():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    res = num1 + num2
    user_res = int(input(" {} + {} = ".format(num1, num2)))
    while (res != user_res):
        user_res = int(input(" {} + {} = ".format(num1, num2)))

    print("True")


repeat_add()
