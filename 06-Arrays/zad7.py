arr=[1,2,3,4,5]
print(arr)
arr[0]=arr[0]-1
arr[-1]=arr[-1]+4
x=int((len(arr)-1)/2)
arr[x]=arr[x]*2
for i in range(0,len(arr)):
    arr[i]+=3
print(arr)