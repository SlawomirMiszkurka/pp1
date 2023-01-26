def f(n1,n2,n3,n4):
    a=[n1,n2,n3,n4]
    counter=0
    for i in a:

        if i<0:
            counter +=1
    return counter==2
print(f(-2,9,-5,7))
print(f(-2,-9,4,-5))