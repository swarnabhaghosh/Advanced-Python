fruits=["apple", "mango", "litchi", "pineapple", "banana", "grape"]
#dir() in Python returns a list of all attributes and methods of an object. It helps in introspection by showing available properties, including built-in methods and user-defined attributes.
##print(dir(fruits)) 
itr=iter(fruits)
try:
        print(next(itr))
        print(next(itr))
        print(next(itr))
        print(next(itr))
        print(next(itr))
        print(next(itr))
        print(next(itr))#it will not work because here the list ends and return stopIteration exception
        print(next(itr))#same for this
except StopIteration as e:
        print("No more elements in the iterator.")


        