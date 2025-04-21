import csv
fileName = "D:\\Studies\\InputFile.csv"

try:
    with open(fileName, "r") as file:  # With Statement will return an object(file).
        placeHolder = csv.reader(file)
        print(placeHolder)# this statement will print address. As CSV file are iteratable.
        for line in placeHolder:
            print(line)
except FileNotFoundError:
    print("File is not available yet.")
except PermissionError:
    print("You don't have permission to read")