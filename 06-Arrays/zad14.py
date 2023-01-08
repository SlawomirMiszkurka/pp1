arr=[[0,0,0],[0,0,0],[0,0,0]]
j=0
for i in arr:
    arr[j][j]=1
    j+=1
for i in arr:
    for j in i:
        print(j,end=' ')
    print()