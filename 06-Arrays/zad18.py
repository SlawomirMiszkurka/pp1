arr=[15, 8, 31, 47, 2, 19]

sum=0
print(arr)
count=len(arr)
while len(arr)!=0:
    sum+=arr[0]
    arr.pop(0)
print(f'Arithmetic mean: {sum/count}')