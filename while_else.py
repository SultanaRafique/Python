import os
print(os.getcwd())
num = 0
while num < 10:
    print("num is less than 10", num)
    if num == 9:
        break
    num+=1
else:
    print("num is not less than 10", num)
