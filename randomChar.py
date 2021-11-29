import random

c1 = input("enter character1: ")
c2 = input("enter character2: ")


def rand_num(ch1, ch2):
    return chr(random.randint(ord(ch1), ord(ch2)))


print(rand_num(c1, c2))
