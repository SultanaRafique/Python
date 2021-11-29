num = input("please enter a number: ")
num = int(num)


def sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0


res = sign(num)
print(res)