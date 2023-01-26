def f(filname):
    x=filname.split('.') 
    return x[0]
print(f("figure.py"))
print((f("Product.java")))