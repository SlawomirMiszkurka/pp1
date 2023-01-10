file=open('products.txt','a')
while True:
    x=input('Add next product ')+'\n'
    if x=='\n':
        break
    file.write(x)
    # file.write('\n')
