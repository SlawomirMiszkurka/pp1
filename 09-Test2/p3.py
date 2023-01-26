def f(array2D):
    arr=[]
    i=0
    while i!=len(array2D[0]):
        sum=0
        for j in array2D:
            sum+=j[i]
        arr.append(sum)
        i+=1
    return arr


print(f([   [3,6,2,7], [9,5,4,0], [2,8,0,9]]))