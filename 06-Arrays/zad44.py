def convert(arr):
    print(f'Original array: {arr}')
    a = []
    for i in arr:
        for j in i:
            a.append(j)
    print(f'Converted array: {a}')


convert([[2, 3], [1, 5]])
convert([[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]])
convert([[2, 1], [3, 5], [7, 4], [2, 6]])
