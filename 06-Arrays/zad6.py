import random
arr = [2, 3, 7, 5, 4]
print(arr)
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[-1])
print(arr[-2])
print(arr[0]+arr[-1])
print(arr[int((len(arr)-1)/2)])
for i in arr:
    print(i, end=' ')
print()
for i in range(0, arr.index(arr[int((len(arr)-1)/2)])+1):
    print(arr[i], end=' ')
