import json
with open('students.json') as file:
    main=json.load(file)
    limited=[]
    for i in main:
        limited.append({'name':i['first_name'],'surname':i['last_name'],'id':i['student ID']})
    with open('limited.json','w') as copy:
        copy.write(json.dumps(limited))
print(limited)