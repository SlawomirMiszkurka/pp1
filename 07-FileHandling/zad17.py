with open('dummytext.txt') as file:
    with open('copylines.txt','w') as copy:
        for line in file:
            copy.write(line)