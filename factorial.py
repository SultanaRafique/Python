num = input("enter num: ")
num = int(num)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


res = factorial(num)
print(res)
