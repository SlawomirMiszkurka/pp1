arr = [[-38, 19], [5, 40], [-76, 11], [29, 16]]
a = [0][0]
b = [0][0]
for i in arr:
    for j in i:
        if j < a:
            a = j
        if j > b:
            b = j
print(f'Array: {arr}')
for i in arr:
    for j in i:
        try:
            j == a
            print(
                f'Lowest value: {a} Row: {arr.index(i)+1}, Column: {i.index(a)+1}')
            a = "Done"
        except ValueError:
            True
        try:
            j == b

            print(
                f'Largest value: {b} Row: {arr.index(i)+1}, Column: {i.index(b)+1}')
            b = 'Done'
        except ValueError:
            True
