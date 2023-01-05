def f(number, even):
    sum = 0
    number = str(number)
    for i in number:
        if even == True:
            if int(i) % 2 == 0:
                sum += int(i)
        else:
            if int(i) % 2 != 0:
                sum += int(i)
    print(sum)


f(3124, True)
f(3124, False)
f(20576, False)
f(20576, True)
f(13115, True)
