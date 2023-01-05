def f(amount_to_pay):
    five = amount_to_pay // 5
    two = (amount_to_pay-five*5) // 2
    one = amount_to_pay-five*5-two*2
    print(five+two+one)


f(23)
f(8)
f(2)
f(0)
