def cal_bmi(age, weight, height):
    if age < 16:
        print("under age")
        return

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        print("UnderWeight")
    elif bmi <= 18.5 and bmi < 25.0:
        print("Normal")
    elif bmi <= 25.0 and bmi < 30.0:
        print("OverWeight")
    elif bmi <= 30.0:
        print("Obese")
    else:
        print("none")


age = int(input("Enter Age: "))
weight = int(input("Enter Weight in Pounds: "))
height = int(input("Enter Inches: "))

cal_bmi(age, weight, height)
