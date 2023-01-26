def f(human_age):
    dogs_age=0
    for i in range(1,human_age+1):
        if i<3:
            dogs_age+=10
        else:
            dogs_age+=4
    return dogs_age
print(f(15))
print(f(2))
