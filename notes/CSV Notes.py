import csv


def validate(num: str):
    if divisible_by_2(num) and divisible_by_3(num):
        return True
    return False


def divisible_by_3(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


"""""
with open("Book1.csv") as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        print("Writing file...   ")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing.....")

        for row in reader:
            # old_number = int(row[0]) + 1
            old_number = row(0)
            new_number = old_number + 1
            row[0] = new_number
            writer.writerow(row)
            # print(old_number)

print("OK")
"""
with open("Book1.csv") as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing.....")

    for row in reader:
        # old_number = int(row[0]) + 1
        old_number = row(0)
        if validate(old_number):
            writer.writerow(row)
print("Done")
