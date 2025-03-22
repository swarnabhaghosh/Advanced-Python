class myException(Exception):
        def __init__(self, *args):
                self.args=args
        def print_message(self):
                print("user defined exception:", self.args)

try:
        raise myException("error is raised")
except myException as e:
        e.print_message()