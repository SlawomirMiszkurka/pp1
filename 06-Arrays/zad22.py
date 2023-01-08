def bubblesort(array):
    arr=[]
    while array!=[]:
        a=array[0]
        for i in array:
            if a>i:
                a=i
        array.pop(array.index(a))
        arr.append(a)
    print(arr)
bubblesort([43,65,23,78,996,22,-34])
bubblesort([-65,54,2,-4,-56,62,9,1])



