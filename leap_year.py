def is_leap_year(year):
    if (year % 4 == 0 or year % 400 == 0 ) and (year % 100 != 0):
        print("{} is leap year".format(year))
    else:
        print("{} is not leap year".format(year))


year = int(input("Enter year: "))
is_leap_year(year)