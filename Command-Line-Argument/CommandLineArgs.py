import argparse

if __name__=="__main__":
        parser = argparse.ArgumentParser() #ArgumentParser() is a method of argparse package, which creates a new argument parser object.
        #this is how we add the arguments to the parser:
        parser.add_argument("number1", help="first number")
        parser.add_argument("number2", help="second number")
        parser.add_argument("operation", help="operation")
        args=parser.parse_args() #this is an obejct which has the value of the arguments
        print(args.number1)
        print(args.number2)
        print(args.operation)


n1=int(args.number1)
n2=int(args.number2)
result=None
try:
        if args.operation=="add":
                res=n1+n2
        elif args.operation=="sub":
                res=n1-n2
        elif args.operation=="mul":
                res=n1*n2
        elif args.operation=="div":
                if n2==0:
                        raise ZeroDivisionError
                res=n1/n2
except ZeroDivisionError as e:
        print("the denomenator is '0'")
finally:
        print("result=",result)
        print("end")