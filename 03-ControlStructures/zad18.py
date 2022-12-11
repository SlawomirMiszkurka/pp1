print("Podaj kwotę w pełnych złotówkach")
x = int(input())
piec = x//5
dwa = ((x-(5*piec))//2)
jeden = ((x-(5*piec)-2*dwa))
print(f"5zł :{piec} \n2zł {dwa} \n1zł: {jeden}")
