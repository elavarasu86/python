
'''An iterator in Python is an object used to traverse through all the elements of a collection (like lists, tuples or dictionaries) one element at a time. It follows the iterator protocol, which involves two key methods:

__iter__(): Returns the iterator object itself.
__next__(): Returns the next value from the sequence. Raises StopIteration when the sequence ends.

Why do we need iterators?
Here are some key benefits:

Lazy Evaluation: Processes items only when needed, saving memory.
Generator Integration: Pairs well with generators and functional tools.
Stateful Traversal: Keeps track of where it left off.
Uniform Looping: Same for loop works for lists, strings and more.
Composable Logic: Easily build complex pipelines using tools like itertools.

'''


#Built-in Iterator Example
#Let’s start with a simple example using a string. We will convert it into an iterator and fetch characters one by one:
    
s = "GFG"
it = iter(s)

print(next(it))
print(next(it))
print(next(it)) 

'''
Explanation:

s is an iterable (string).
iter(s) creates an iterator.
next(it) retrieves characters one by one
'''


'''
Creating a Custom Iterator
Creating a custom iterator in Python involves defining a class that implements the __iter__() and __next__() methods according to the Python iterator protocol.

Steps to follow:

Define the Class: Start by defining a class that will act as the iterator.
Initialize Attributes: In the __init__() method of the class, initialize any required attributes that will be used throughout the iteration process.
Implement __iter__(): This method should return the iterator object itself. This is usually as simple as returning self.
Implement __next__(): This method should provide the next item in the sequence each time it's called.
Below is an example of a custom class called EvenNumbers, which iterates through even numbers starting from 2:
'''
    
class EvenNumbers:
    def __iter__(self):
        self.n = 2  # Start from the first even number
        return self

    def __next__(self): # Advantage is customization. We can have our own custom logic.
        x = self.n
        self.n += 2  # Increment by 2 to get the next even number
        return x

# Create an instance of EvenNumbers
even = EvenNumbers()
it = iter(even)# This line of code will call __iter__ fn and return iterable object.

# Print the first five even numbers
print(next(it))  #Line call's __next__ fn.
print(next(it)) 
print(next(it))  
print(next(it)) 
print(next(it))

#above code can be rewritten like below.

for num in even:
    print(num)

'''
Explanation:

Initialization: The __iter__() method initializes the iterator at 2, the first even number.
Iteration: The __next__() method retrieves the current number and then increases it by 2, ensuring the next call returns the subsequent even number.
Usage: We create an instance of EvenNumbers, turn it into an iterator and then use the next() function to fetch even numbers one at a time.
'''


'''
StopIteration Exception
StopIteration exception is integrated with Python’s iterator protocol. It signals that the iterator has no more items to return. Once this exception is raised, further calls to next() on the same iterator will continue raising StopIteration.
'''

li = [100, 200, 300]
it = iter(li)

# Iterate until StopIteration is raised
while True:
    try:
        print(next(it))
    except StopIteration:
        print("End of iteration")
        break