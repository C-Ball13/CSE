import csv

with open("Sales Records.csv") as old_csv:
        reader = csv.reader(old_csv)
        for row in reader:
            old_number = row[2]
            print(old_number)
