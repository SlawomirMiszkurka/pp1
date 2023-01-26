import csv

with open('students.txt', 'r') as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        if int(row[2])<30:
            print(f'{row[0]} {row[1]} {row[4]}')
    