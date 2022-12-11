PIN = "0805"
i = 0
while True:

    if i == 3:
        print("Sorry, your payment card has been blocked.")
        break
    print("Podaj PIN: ")
    x = input()
    if x == PIN:
        print("Correct")
        break
    else:
        print("Incorrect try again.")
        i += 1
