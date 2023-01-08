arr=[[True,False],[True,True],[False,False]]
print(arr)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]==True:
            arr[i][j]=False
        else:
            arr[i][j]=True
print(arr)