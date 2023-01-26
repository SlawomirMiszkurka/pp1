import re
with open('grades.txt') as file:
    grades=re.findall('\d.\d',file.read())
    sum=0
    for i in grades:
        sum+=float(i)
    
print(f"""Arithmetic mean of student's grades: {round(sum/len(grades),2)}""")