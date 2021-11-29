def predict_tuition(tuition, per):
    counter = 0
    year_tuition = tuition
    while year_tuition < (2 * tuition):
        year_tuition *= per
        counter = counter + 1

    return counter


user_input = int(input("Enter tuition fee: "))
percent = int(input("Enter percent: "))
percent = (percent / 100.0) + 1.0
res = predict_tuition(user_input, percent)
print(res)
