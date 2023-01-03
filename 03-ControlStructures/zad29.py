quantity=0
sum=0
while True:
    a=int(input())
    if a==0:
        print(f"Result: Quantity=: {quantity}, Sum={sum}, Mean={sum/quantity}")
        break
    else:
        print(f"Enter number: {a}" )
        sum=sum+a
        quantity +=1

