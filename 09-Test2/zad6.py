import json
def f(name,surname):
    with open("data.json") as file:
        max=0
        file=json.load(file)
        
        for i in file:
            if i["name"]==name and i["surname"]==surname:
                for j in i["studies"]["courses"]:
                    sum=0
                    for k in j["grades"]:
                        sum+=k
                    x=(sum/len(j["grades"]))
                    if max<x:
                        max=x
                        output=j["name"]
    return output

print(f("Urbano","Rossander"))
print(f("Minnie","Mesant"))