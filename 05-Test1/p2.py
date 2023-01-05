def f(binary_numbers):
    x = True
    for i in binary_numbers:
        if i != "0" and i != "1":
            x = False
            break
    print(x)


f("101101")
f("1311a10100")
