arr = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [6, 7, 8, 9, 0]]
print(arr)
for i in arr:
    a = i[0]
    i[0] = i[-1]
    i[-1] = a

print(arr)
