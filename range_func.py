def range_func1(n):
    for i in range(n):
        print("hello world", i)


def range_func2(num1, num2):
    for i in range(num1, num2):
        print("hello world", i)


def range_func3(num1, num2, step):
    for i in range(num1, num2, step):
        print("hello world", i)




print("-------range(num)--------")
range_func1(11)

print("-------range(num1, num2)--------")
range_func2(5, 11)

print("-------range(num1, num2, step)--------")
range_func3(10, 101, 10)