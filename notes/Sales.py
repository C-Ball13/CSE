import csv

with open("Sales Records.csv", 'r') as old_csv:
        reader = csv.reader(old_csv)
        fruits = 0
        for row in reader:
            old_number = row[2]
            print(old_number)
