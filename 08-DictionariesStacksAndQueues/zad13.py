import json
student={
    'name':'Jane',
    'surname':'Doe',
    'age': 22,
    'idNumber': 987654,
    'activeStudent':True
}
with open('student.json','w') as file:
    # file.write(json.dumps(student))
    json.dump(student,file)