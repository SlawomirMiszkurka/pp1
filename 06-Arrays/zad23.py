arr=[2,3,2,5,8,1,9,8]
for i in arr:
    count=0
    for j in range(len(arr)):
        if i==arr[j]:
            count+=1
    if count>1:
        while True:
            try:
                arr.pop(arr.index(i))
            except ValueError:
                break
print(arr)