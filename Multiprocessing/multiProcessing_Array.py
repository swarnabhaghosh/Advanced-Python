# Sharing Data Between Processes Using Array and Value
# if we try to print a global variable inside a process it will be doing ok but for outside the process this will not work, because when we create a new process from a parent process it creates its own adress space (where it stores all thes variables etc.), where the global variable is the part of the main (parent) process, it will be not accessible by the new process
# to resolve this process we require IPC: (Inter-process Communication) usinfg files, queues, message pipes, shared memory [array, value] instead of global variable

# shared memory variable is different from regular variables and need to mention the datatype while created, (for integer it is 'i' and for double it is 'd') and the size of the input, It is not resizable (fixed size when created).

# multiprocessing.Array is shared across processes.
# It is synchronized, so modifications are reflected.

# Array is a shared memory 

import multiprocessing

def square(numbers, result):
        for idx, number in enumerate(numbers):  #enumerate returns both index and element
                result[idx]=number*number

if __name__=="__main__":
        arr=[2,3,4,5]
        result=multiprocessing.Array('i',4) #this is the shared memory variable, and the datatype is integer('i') and the size of input is 4
        p=multiprocessing.Process(target=square,args=(arr, result)) #pass the shared memory variable into the process
        # Starting threads
        p.start() 
        # Waiting for both threads to finish
        p.join()
        print("outside process ",result[:]) #technique of printing an array
        print("done")