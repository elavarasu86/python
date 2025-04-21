
try:
    # My default WITH sttement will close the open file.
    with open('D:\\Studies\\Application_SQ_Transformation.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("File not available Yet.")

#Return's boolean value. True is closed. False is Open.
#print(file.closed)