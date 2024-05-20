import csv

data = csv.reader(open('csv/students.csv','r'))
for row in data:
    print(row)