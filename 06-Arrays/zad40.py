arr = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [6, 7, 8, 9, 0]]
a = []
print(arr)
a.append(arr[0])
arr[0] = arr[-1]
arr[-1] = a[0]
print(arr)
