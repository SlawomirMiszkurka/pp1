arr=[15, 8, 31, 47, 2, 19]
newarr=[]
print(f'Existed array: {arr}')
for i in range(len(arr)):
    newarr.append(arr[-1-i])
print(f'Reverse array: {newarr}')