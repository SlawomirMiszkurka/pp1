def f(number, even):
    suma = 0
    number = str(number)
    if even == True:
        for i in range(len(number)):
            if int(number[i]) % 2 == 0:
                suma = suma+int(number[i])

    elif even == False:
        for i in range(len(number)):
            if int(number[i]) % 2 != 0:
                suma = suma+int(number[i])
    print(suma)


f(3124, True)
f(3124, False)
f(20576, False)
f(20576, True)
f(13115, True)
