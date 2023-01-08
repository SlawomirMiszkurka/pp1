arr=[[2,5,4],[9,0,3]]
print(arr)
print(f'Columns: {len(arr)}, Rows: {len(arr[0])}')
print(arr[1][1])
for i in arr[1]:
    print(i,end=' ')
print()
for i in arr:
    for j in arr[arr.index(i)]:
        print(j,end=' ')
    print()
for i in range(0,2):
    print(arr[i][-1])