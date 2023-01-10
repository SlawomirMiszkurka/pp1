def transponse_matrix(m):
    a = []

    try:
        counter = 0
        while counter < len(m[0]):
            arr = []
            for i in m:
                arr.append(i[counter])
            a.append(arr)
            counter += 1

    except TypeError:
        for i in m:
            arr = []
            arr.append(i)
            a.append(arr)
    print(a)


transponse_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
transponse_matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
transponse_matrix([5, 6, 7, 8])
