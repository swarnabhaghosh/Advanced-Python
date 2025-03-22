# dividing work equally to the cores of the CPU, utilising the CPU totally is called Parallel processing. 
# In Parallel processing, dividing the inputs between the multiple units (cores) is called Map and aggregating the results back is called Reduce
'''
import multiprocessing
import time

def func(n):
        sum=0
        for i in range(1000):
                sum+=i*i
        return sum

if __name__=="__main__":
        t1=time.time()
        p=multiprocessing.Pool()
        result1=p.map(func, range(10000))
        p.close()
        p.join()
        #print(result1)
        print("Pool took=", time.time()-t1)

        t2=time.time()
        result2=[]
        for i in range(10000):
                result2.append(func(i))
        #print(result2)
        print("serial processing took=",time.time()-t2)


'''
from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(n):
        sum += x * x
    return sum

if __name__ == "__main__":
    t1 = time.time()
    p = Pool()
    result = p.map(f, range(10000))
    p.close()
    p.join()

    print("Pool took:", time.time() - t1)

    t2 = time.time()
    result = []
    for x in range(10000):  
        result.append(f(x))

    print("Serial processing took:", time.time() - t2)


#pool takes lesser time than serial process