y=input('enter a number:')
try:
    s=float(y)
    inverse=1.0/s
    print(inverse)
except ValueError:
    print('not a number!')
except ZeroDivisionError:
    print('infinity')
finally:
          print('always execute')
