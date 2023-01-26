import random
with open('intigers100-999.txt','w') as file:
    for i in range(1,51):
        file.write((str(random.randint(100,999))+'\n'))