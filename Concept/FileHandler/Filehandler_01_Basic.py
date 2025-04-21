
try:
    # My default WITH sttement will close the open file.
    with open('D:\\Studies\\Application_SQ_Transformation.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("File not available Yet.")

#Return's boolean value. True is closed. False is Open.
#print(file.closed)


######################################################################################
fileName = "D:\\Studies\\InputFil.txt"

try:
    with open(fileName, "r") as file:  # With Statement will return an object(file).
        placeHolder = file.read()
        print(placeHolder)
except FileNotFoundError:
    print("File is not available yet.")
except PermissionError:
    print("You don't have permission to read")
