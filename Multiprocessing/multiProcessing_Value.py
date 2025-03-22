#Value is a shared memory 
'''
value and Value are different in Python's multiprocessing module.

🔹 Difference Between Value and value:

##Value (with uppercase 'V')
"multiprocessing.Value" is a class used to create a shared variable between processes.

Example:
balance = multiprocessing.Value('i', 200)  # 'i' means integer type


##value (with lowercase 'v')
".value" is an attribute of a 'multiprocessing.Value' object. It is used to access or modify the stored value.

Example:
balance.value += 1  # Access and update the shared variable

🔹 Summary
✅ Value('i', 200) → Creates a shared memory variable.
✅ balance.value → Accesses or modifies the stored integer in shared memory.

 So, Value is a method (class), and value is an attribute of the shared variable!
'''

import multiprocessing

def square(numbers, result, v):
        v.value=69.69 #here the value is being changed inside the process
        for idx, number in enumerate(numbers):  #enumerate returns both index and element
                result[idx]=number*number
if __name__=="__main__":
        arr=[2,3,4,5]
        result=multiprocessing.Array('i', 4) #this is the shared memory variable (array), and the datatype is integer('i') and the size of input is 4
        v=multiprocessing.Value('d', 0.0) #this is the shared memory (value), and the value passed is 0.0 (as default)
        p=multiprocessing.Process(target=square,args=(arr, result, v)) #pass the shared memory variable into the process
        # Starting threads
        p.start() 
        # Waiting for both threads to finish
        p.join()
        print("value=",v.value)
        print("outside process ",result[:]) #technique of printing an array
        print("done")