def break_stmt(n):
    for i in range(n):
        if i == 5:
            continue
        print("Hello ", i)


break_stmt(11)