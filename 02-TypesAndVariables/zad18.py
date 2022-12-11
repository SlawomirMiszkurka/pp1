print("Podaj długość boku a")
a = int(input())
print("Podaj długość boku b")
b = int(input())
print("Podaj długość boku c")
c = int(input())
obw = (a+b+c)/2
pole = (obw*(obw-a)*(obw-b)*(obw-c))**(1/2)
print(f'Pole trójkąta wynosi {pole}')
