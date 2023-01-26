with open('shoppinglist.txt','a') as main:
    with open('MeatAndFish.txt') as file:
        with open('GrainsAndBread.txt') as file1:
            main.write(file.read())
            main.write(file1.read())