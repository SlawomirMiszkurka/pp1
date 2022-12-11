def f(binary):

    for i in range(len(binary)):
        if binary[i] != '0' and binary[i] != '1':
            print(False)
            break
        elif i == len(binary)-1:
            print(True)
        i += 1


f("1110a100")
