def compare(array1,array2):
    if len(array1)!=len(array2):
        print(f'{array1}\n{array2}\nComparison: arrays are different')
    else:
        for i in range(len(array1)):
            if array1[i]!=array2[i]:
                print('Arrays are different')
                break
        print(f'{array1}\n{array2}\nComparison: arrays are the same')

compare(["water","book","sky"],["water","book","sky"])
compare([True,False],[True,False,True])
compare([5,3,1],[5,3,1])
compare([3,2,1],[3,2])

