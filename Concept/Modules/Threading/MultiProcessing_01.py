from multiprocessing import Pool
'''
The Pool class in python's Multiprocessing modul manages a pool of worker processes to execute tasks concurrently. 
'''

def squareroot(x):
    print(x)
    return x*x

if __name__=="__main__":
    print(squareroot(5))
    #1.     Initialization: When you create Pool object, it initializes a specified number of worker processes.
    #       These processes a created and start running, waiting for tasks to be assigned.
    #        Example( with Pool(5) as P:
    with Pool(5) as P:
        #2.     Task Assignment: When you use methods like map,apply or starmap the Pool distributes the task amoung the worker processes. 
        #       Map takes a function and an iterable, and applies the function to each element of the iterable in parallel.
        
        #3.     Task Execution: Each worker process picks up tasks from a queue, executes them, and returns the results. the processes do not exit after completing a task.
        #       They return to waiting state, ready to pick up new taks.
        
        #4.     Result collection: the results from the worker processes are collected and returned to the main process.
        #       Methods like Map blocks until all tasks are completed., while methods like map_async allow for non-blocking execution.
        
        results = P.map(squareroot,[1,2,3,4,5,6,7,8])
        
        #5.     Process Management: The Pool class includes mechanisms to manage the lifecycle of worker processes.
        #       For Example you can use the maxtaskperchild parameter to specify the maximum number of tasks a worker process can handle before it is replaced with a new one.
        
    print(results)