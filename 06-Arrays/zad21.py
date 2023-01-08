arr1=[4,36,12,28,9,44,5]
arr2=[5,1,36]
for i in arr2:
    try:
        arr1.pop(arr1.index(i))
    except ValueError:
        continue
print(arr1)