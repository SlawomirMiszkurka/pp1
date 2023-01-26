def f(array2D):
    i=0
    arr=[]
    while i<len(array2D[0]):
        count=0
        for j in array2D:
            count+=j[i]
        arr.append(count)
        i+=1
    max=arr[0]
    for i in arr:
        if i>max:
            max=i
    return arr.index(max)
print(f([[6,8],[9,5]]))
print(f([[8,7,8,5],[7,5,9,4]]))
print(f([[6,8],[9,5],[5,9]]))