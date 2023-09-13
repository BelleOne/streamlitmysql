import csv

with open('filedata/simple.csv', 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=',')
    for row in csv_reader:
        print(row['year'], row['sela_amount'])
