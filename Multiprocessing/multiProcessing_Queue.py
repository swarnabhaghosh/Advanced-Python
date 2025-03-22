#Queue is a shared memory 

import multiprocessing

def square(numbers, q):
        for number in numbers: 
                q.put(number*number) #inserting in Queue


if __name__=="__main__":
        numbers=[2,3,4,5]
        q=multiprocessing.Queue() #this is a shared memory variable, no datatype or size is required
        p=multiprocessing.Process(target=square,args=(numbers, q)) #pass the shared memory variable into the process
        # Starting threads
        p.start() 
        # Waiting for both threads to finish
        p.join()
        while q.empty() is False:
                print(q.get()) #printing a Queue
        print("done")