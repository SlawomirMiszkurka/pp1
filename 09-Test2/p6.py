import json
def f(age, course, average):
    with open("data.json") as file:

        file=json.load(file)
        counter=0
        for i in file:
            if i["age"]>=age:
                for j in i["studies"]["courses"]:
                    avg=0
                    if (j["name"]==course):
                        for k in j["grades"]:
                            avg+=k
                    avg1=avg/len(j["grades"])
                    if avg1>=average:
                        counter+=1
    return counter

print(f(21,"statistics",4))