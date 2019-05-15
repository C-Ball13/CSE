import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    fruits = 0
    clothes = 0
    meat = 0
    beverages = 0
    office_supplies = 0
    cosmetics = 0
    snacks = 0
    personal_care = 0
    household = 0
    vegetables = 0
    baby_food = 0
    cereal = 0
    print("Processing......")
    for row in reader:
        if row[2] == "Cosmetics":
            profits = float(row[13])
            for i in row[13]:
                cosmetics += 1
        elif row[2] == "Snacks":
            profits = float(row[13])
            for i in row[13]:
                snacks += 1
        elif row[2] == "Snacks":
            profits = float(row[13])
            for i in row[13]:
                snacks += 1
        elif row[2] == "Snacks":
            profits = float(row[13])
            for i in row[13]:
                snacks += 1
        elif row[2] == "Snacks":
            profits = float(row[13])
            for i in row[13]:
                snacks += 1
        elif row[2] == "Snacks":
            profits = float(row[13])
            for i in row[13]:
                snacks += 1
        elif row[2] == "Snacks":
            profits = float(row[13])
            for i in row[13]:
                snacks += 1
        elif row[2] == "Snacks":
            profits = float(row[13])
            for i in row[13]:
                snacks += 1
        elif row[2] == "Snacks":
            profits = float(row[13])
            for i in row[13]:
                snacks += 1
        elif row[2] == "Snacks":
            profits = float(row[13])
            for i in row[13]:
                snacks += 1
        elif row[2] == "Snacks":
            profits = float(row[13])
            for i in row[13]:
                snacks += 1
        elif row[2] == "Snacks":
            profits = float(row[13])
            for i in row[13]:
                snacks += 1