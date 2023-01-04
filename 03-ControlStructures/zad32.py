for i in range(1, 8):
    for j in range(0, 49, 7):
        if i+j < 10:
            print(f' {i+j}', end=" ")
        else:
            print(i+j, end=" ")
    print()
