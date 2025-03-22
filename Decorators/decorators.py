import time

def time_it(func): #function as input
    def wrapper(*args, **kwargs): #nested function
        #*args for arguments and **kwargs for keywords
        start = time.time() #time before starting func
        result = func(*args, **kwargs)  # Call the original function
        end = time.time() #time after ending func
        print(f"{func.__name__} took {(end - start) * 1000:.5f} milliseconds")  # Print execution time
        return result  # Return the actual function result
    return wrapper

@time_it
def square(numbers):
    return [number ** 2 for number in numbers]

@time_it
def cube(numbers):
    return [number ** 3 for number in numbers]

array = list(range(1, 101))

out_square = square(array)
out_cube = cube(array)
#print(out_square[:5])  # Print first 5 elements to check
#print(out_cube[:5])    # Print first 5 elements to check
