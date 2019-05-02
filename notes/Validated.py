import csv


def validate(num: str):
    if len(num) == 16:
        with open("Book1.csv") as old_csv:
            with open("MyNewFile.csv", "w", newline='') as new_csv:
                reader = csv.reader(old_csv)
                writer = csv.writer(new_csv)
                print("Processing.....")

            for row in reader:
                old_number = row(0)
                if validate(old_number):
                    writer.writerow(row)
        print("Done")


print(validate("5241329116205410"))

list_num = list(number)
for index in range(len(number)):
    list_num[index] = int(list_num[index])
