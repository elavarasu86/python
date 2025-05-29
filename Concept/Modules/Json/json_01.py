import json

'''
The with statement in Python is used for resource management and exception handling. 
It simplifies working with resources like files, network connections and database connections by ensuring they are properly acquired and released. 
When we open a file, we need to close it ourself using close(). But if something goes wrong before closing, the file might stay open, causing issues. 
Using with open() automatically closes the file when we're done, even if an error happens.
'''

# we are opening the json file in read mode.
with open('data.json','r') as file:
    data = json.load(file)
    
#prints json file as it reads.
print(data)