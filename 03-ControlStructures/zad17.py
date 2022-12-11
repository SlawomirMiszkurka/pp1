x = int(input("Wprowadź pierwszą współrzędną: "))
y = int(input("Wprowadź drugą współrzędną: "))
if x > 0 and y > 0:
    print(f"Punkt P({x},{y}) jest w pierwszej ćwiartce układu współrzędnych")
elif x < 0 and y < 0:
    print(f"Punkt P({x},{y}) jest w trzeciej ćwiartce układu współrzędnych")
elif x < 0 and y > 0:
    print(f"Punkt P({x},{y}) jest w czwartej ćwiartce układu współrzędnych")
elif x > 0 and y < 0:
    print(f"Punkt P({x},{y}) jest w drugiej ćwiartce układu współrzędnych")
elif x == 0 and y != 0:
    print(f"Punkt P({x},{y}) jest na osi y")
elif x != 0 and y == 0:
    print(f"Punkt P({x},{y}) jest na osi x")
else:
    print(f"Punkt P({x},{y}) jest na środku układu współrzędnych")
