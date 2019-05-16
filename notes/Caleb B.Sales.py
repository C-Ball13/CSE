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
        elif row[2] == "Baby Food":
            profits = float(row[13])
            for i in row[13]:
                baby_food += 1
        elif row[2] == "Cereal":
            profits = float(row[13])
            for i in row[13]:
                cereal += 1
        elif row[2] == "Vegetables":
            profits = float(row[13])
            for i in row[13]:
                vegetables += 1
        elif row[2] == "House Hold":
            profits = float(row[13])
            for i in row[13]:
                household += 1
        elif row[2] == "Personal Care":
            profits = float(row[13])
            for i in row[13]:
                personal_care += 1
        elif row[2] == "Office Supplies":
            profits = float(row[13])
            for i in row[13]:
                office_supplies += 1
        elif row[2] == "Meat":
            profits = float(row[13])
            for i in row[13]:
                meat += 1
        elif row[2] == "Fruits":
            profits = float(row[13])
            for i in row[13]:
                fruits += 1
        elif row[2] == "Beverages":
            profits = float(row[13])
            for i in row[13]:
                beverages += 1
        elif row[2] == "Clothes":
            profits = float(row[13])
            for i in row[13]:
                clothes += 1

total_profits = [fruits, clothes, cosmetics, meat, beverages, office_supplies, snacks, personal_care, household,

                 vegetables, baby_food, cereal]

print("The profit for fruits is %d" % fruits)
print("The profit for clothes is %d" % clothes)
print("The profit for meat is %d" % meat)
print("The profit for snacks is %d" % snacks)
print("The profit for household is %d" % household)
print("The profit for cereal is %d" % cereal)
print("The profit for baby food is %d" % baby_food)
print("The profit for vegetables is %d" % vegetables)
print("The profit for personal care is %d" % personal_care)
print("The profit for cosmetics is %d" % cosmetics)
print("The profit for office supplies is %d" % office_supplies)
print("The profit for beverages is %d" % beverages)


if max(total_profits) == fruits:
    print("Fruits had the most profit")
if max(total_profits) == meat:
    print("Meat had the most profit")
if max(total_profits) == beverages:
    print("Beverages had the most profit")
if max(total_profits) == cereal:
    print("Cereal had the most profit")
if max(total_profits) == cosmetics:
    print("cosmetics had the most profit")
if max(total_profits) == clothes:
    print("Clothes had the most profit")
if max(total_profits) == personal_care:
    print("personal Care had the most profit")
if max(total_profits) == vegetables:
    print("Vegetables had the most profit")
if max(total_profits) == baby_food:
    print("Baby Food had the most profit")
if max(total_profits) == office_supplies:
    print("Office supplies had the most profit")
if max(total_profits) == household:
    print("Household had the most profit")
if max(total_profits) == snacks:
    print("Snacks had the most profit")
