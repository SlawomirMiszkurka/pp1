arr=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
length=0
for i in range(0,len(arr)):
    if len(arr[length])<len(arr[i]):
        length=i
print(f'Longest name: {arr[length]}')