import json
fileName = "D:\\Studies\\InputFile.json"

try:
    with open(fileName, "r") as file:  # With Statement will return an object(file).
        placeHolder = json.load(file)
        print(placeHolder)
        print(placeHolder["name"])
except FileNotFoundError:
    print("File is not available yet.")
except PermissionError:
    print("You don't have permission to read")
