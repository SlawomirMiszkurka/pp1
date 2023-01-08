arr=[15, 38, 7, 23, 14]
a=231

print(f'Number: {a}\nArray: {arr}')
try:
    arr.index(a)
    print(f'Result: {a} appears in the array')
except ValueError:
    print(f'Result: {a} isn\'t appears in the array')