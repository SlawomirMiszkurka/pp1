with open('dummytext.txt') as f:
    counter=0
    for line in f:
        if counter%5==0 and counter!=0:
            input('Press Enter to continue...')
        print(line)
        counter+=1