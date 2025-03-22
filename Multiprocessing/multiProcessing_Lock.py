#whenever two processes or threads are trying to access a shared resource (such as memory, files, databases etc.), it creates proble. to protect that access, Lock is used. 
'''
let's take a simple example:
In a banking software suppose there are two processes called deposit and withdraw, if we run both processes at the same time and iterate for same time span, it may happen that one process is occuring before one process instead of occuring simultaneously, it may cause a mess and returns a wrong output
that's why we use "Lock" to prevent this.
'''
import time
import multiprocessing

def deposit(balance, lock):
        for i in range(5):
                time.sleep(0.01)
                lock.acquire() #Lock start
                balance.value+=1#Critical region (the portion between acquire and release)
                lock.release() #Lock released


def withdraw(balance, lock):
        for i in range(5):
                time.sleep(0.01)
                lock.acquire() #Lock start
                balance.value-=1 #Critical region (the portion between acquire and release)
                lock.release() #Lock released


if __name__=="__main__":
        balance=multiprocessing.Value('i', 200)
        lock=multiprocessing.Lock()
        w=multiprocessing.Process(target=withdraw, args=(balance, lock))
        d=multiprocessing.Process(target=deposit, args=(balance, lock))
        w.start()
        d.start()
        w.join()
        d.join()
        print("value=",balance.value)



