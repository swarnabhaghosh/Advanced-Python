import time 
import threading

squarelist=[] #a global variable (list)
def square(numbers):
        print("calculate square numbers:")
        for number in numbers:
                time.sleep(0.2)
                print("square",number*number)
                #squarelist.append(number*number) 
                #storing result of the function into a global variable (list)

def cube(numbers):
        print("calculate cube numbers:")
        for number in numbers:
                time.sleep(0.2)
                print("cube",number*number*number)

arr=[2,3,4,5]

start=time.time()

square(arr)

cube(arr)

end=time.time()

print("it took=",(end-start))
#print(squarelist)--> it works outside of the thread, unlike process 
print("done")