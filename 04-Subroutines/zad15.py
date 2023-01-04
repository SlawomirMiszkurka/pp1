import mymath

x = mymath.generate_number()
while True:
    y = mymath.read_number()
    if y == x:
        print("You WIN")
        break
    print("Try again")
