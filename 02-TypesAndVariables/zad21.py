import random
x = random.randint(1, 6)
print("Zgadnij liczę oczek na kostce")
y = int(input())
if x == y:
    print(True)
else:
    print(False)
