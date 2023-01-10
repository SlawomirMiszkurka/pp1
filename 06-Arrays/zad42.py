def identity_matrix(n):
    a = []
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(0)
        a.append(arr)
        a[i][i] = 1
    print(f'Identity matrix {n}: \n{a}')


identity_matrix(3)
identity_matrix(5)
identity_matrix(8)
