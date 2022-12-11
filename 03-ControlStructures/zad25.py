a = int(input())
b = int(input())

for i in range(a):
    if i == 0 or i == a-1:
        print("*"*b)
    else:
        print("*"+(a-2)*" "+"*")
