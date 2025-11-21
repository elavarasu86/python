
'''
Lambda Functions are anonymous functions means that the function is without a name
    def keyword is used to define a normal function
    lambda keyword is used to define an anonymous function
    
    
Syntax

        lambda arguments : expression
        
        lambda: The keyword to define the function.
        arguments: A comma-separated list of input parameters like in a regular function.
        expression: A single expression that is evaluated and returned.


'''


s1 = 'GeeksforGeeks'
s2 = lambda func: func.upper()# lambda is the keyword, func is the argument, we can pass multiple arguments.
print(s2(s1))


# Using with Condition Checking

n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero" # "Positive" will be returned after checking if condition, if condition not satisfied else will be executed
print(n(5))   
print(n(-3))  
print(n(0))

# Using with List Comprehension

li = [lambda arg=x: arg * 10 for x in range(1, 5)]# this statement create list of lambda fn.
for i in li:
    print(i())# Reason i() used is i is a lambda fn.
    # In above code x will be assigned to arg

# Using for Returning Multiple Results
calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)