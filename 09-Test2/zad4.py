def f(dictionary,average):
    sum=0
    inside_grades=dictionary['subject']['grades']
    for i in inside_grades:
        sum+=i
    return sum/len(inside_grades)>average
print(f({"subject":{"name":"math","grades":[3,3,4]}},3))
print(f({"subject":{"name":"math","grades":[3,3,4]}},4))