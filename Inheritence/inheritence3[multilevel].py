class student:
    def __init__(self,a=None,b=None):
        self.roll=a
        self.name=b
    def student_read(self):
        self.roll=int(input("roll:"))
        self.name=input("name:")
    def student_display(self):
        print("roll:",self.roll)
        print("name:",self.name)

class subject(student):
    def __init__(self,r=None,n=None,m1=None,m2=None,m3=None):
        super().__init__(r,n)
        self.eng=m1
        self.math=m2
        self.computer=m3
    def subject_read(self):
        self.eng=int(input('marks of english:'))
        self.math=int(input('marks of math:'))
        self.computer=int(input('marks of computer:'))
    def subject_display(self):
        print("english:",self.eng)
        print("math:",self.math)
        print("computer:",self.computer)
        

class result(subject):
    def __init__(self,r=None,n=None,m1=None,m2=None,m3=None):
        super().__init__(r,n,m1,m2,m3)

    def result_display(self):
        self.total=self.eng+self.math+self.computer
        self.per=float(self.total/3)
        print("total:",self.total)
        print("per:",self.per)


s=result()

s.student_read()
s.subject_read()
s.student_display()
s.subject_display()
s.result_display()

s1=result(11,"ramu",78,67,98)
s1.student_display()
s.subject_display()
s1.result_display()
