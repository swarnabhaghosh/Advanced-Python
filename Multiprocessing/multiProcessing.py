import time 
import multiprocessing

def square(numbers):
        print("calculate square numbers:")
        for number in numbers:
                time.sleep(0.2)
                print("square",number*number)
def cube(numbers):
        print("calculate cube numbers:")
        for number in numbers:
                time.sleep(0.2)
                print("cube",number*number*number)

arr=[2,3,4,5]

p1=multiprocessing.Process(target=square,args=(arr,))
p2=multiprocessing.Process(target=cube,args=(arr,))

start=time.time()

# Starting threads
p1.start()
p2.start() 

# Waiting for both threads to finish
p1.join()
p2.join()

end=time.time()
print("it took=",(end-start))
print("done")