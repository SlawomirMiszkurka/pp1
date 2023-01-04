def power(x, n):
    if n == 1:
        return x
    suma = x*power(x, n-1)
    return suma


print(power(5, 3))
