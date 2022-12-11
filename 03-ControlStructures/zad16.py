def sort(a, b):
    if a < b:
        print("Numery w kolejności rosnącej", a, b)
    else:
        print("Numery w kolejności rosnącej", b, a)


print("Podaj 2 liczby")
a = int(input())
b = int(input())
sort(a, b)
