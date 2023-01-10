x=input('File name: ')
f=open(x)
count=0
for line in f:
    count+=1
print(f'Noumber of lines: {count}')