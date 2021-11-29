def compute_tax(status, income):
    tax = 0
    if status == 0:
        if income > 0 and income <= 8350:
            tax = 10
        elif income <= 33950:
            tax = 15
        elif income <= 82250:
            tax = 25
        elif income <= 171550:
            tax = 28
        elif income <= 372950:
            tax = 33
        elif income > 372951:
            tax = 35
    elif status == 1:
        if income > 0 and income <= 16700:
            tax = 10
        elif income <= 67900:
            tax = 15
        elif income <= 137050:
            tax = 25
        elif income <= 208850:
            tax = 28
        elif income <= 372950:
            tax = 33
        elif income > 372951:
            tax = 35
    elif status == 2:
        if income > 0 and income <= 8350:
            tax = 10
        elif income <= 33950:
            tax = 15
        elif income <= 68525:
            tax = 25
        elif income <= 104425:
            tax = 28
        elif income <= 186475:
            tax = 33
        elif income > 186476:
            tax = 35

    elif status == 3:
        if income > 0 and income <= 11950:
            tax = 10
        elif income <= 45500:
            tax = 15
        elif income <= 117450:
            tax = 25
        elif income <= 190200:
            tax = 28
        elif income <= 372950:
            tax = 33
        elif income > 372951:
            tax = 35
    else:
        print("wrong status")

    return (tax / 100) * income


status = int(input("please enter status: "))
income = int(input("please enter income: "))
res = compute_tax(status, income)
print(res)
