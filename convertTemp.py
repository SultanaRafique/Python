temp_f = input("please enter Fahrenheit Temperature:")
temp_f = float(temp_f)


def convert_temp(temp):
    return (temp - 32) * (5.0 / 9.0)


res = convert_temp(temp_f)
print(res)
