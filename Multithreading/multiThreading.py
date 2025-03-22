import time 
import threading

squarelist=[] #a global variable (list)
def square(numbers):
        print("calculate square numbers:")
        for number in numbers:
                time.sleep(0.2)
                print("square",number*number)
                squarelist.append(number*number) #storing result of the function into a global variable (list)
def cube(numbers):
        print("calculate cube numbers:")
        for number in numbers:
                time.sleep(0.2)
                print("cube",number*number*number)

arr=[2,3,4,5]

thread1=threading.Thread(target=square,args=(arr,))
thread2=threading.Thread(target=cube,args=(arr,))

start=time.time()

# Starting threads
thread1.start()
thread2.start()

# Waiting for both threads to finish
thread1.join()
thread2.join()

end=time.time()
print("it took=",(end-start))
#print(squarelist)--> it works outside of the thread, unlike process 
print("done")