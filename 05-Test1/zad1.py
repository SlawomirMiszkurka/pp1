def f(card_number):
    if len(card_number) == 16:
        x = card_number[0:2]+10*"*"+card_number[12:]
    print(x)


f("5290312400019022")
