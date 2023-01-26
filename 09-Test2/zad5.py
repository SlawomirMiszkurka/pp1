import pandas 

def f(name, surname):
    data = pandas.read_csv('data.csv')
    person = data[(data['name'] == name) & (data['surname'] == surname)]
    return [person['gender'].values[0], person['carcolor'].values[0]]
print(f("Burk","Servis"))
print(f("Evaleen","Uttridge"))