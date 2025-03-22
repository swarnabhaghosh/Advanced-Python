class emp:
    def __init__(self):
        self.__empid=0
        self.__ename=""
        self._basic=0
    def emp_read(self):
        self.__empid=int(input("empid:"))
        self.__ename=input("ename:")
        self._basic=int(input("basic:"))
    def emp_display(self):
        print("empid:",self.__empid)
        print("ename:",self.__ename)
        print("basic:",self._basic)

class payslip(emp):
    def __init__(self):
        super().__init__()
    def calculation(self):
        self.da=self._basic*.40
        self.hra=(self._basic+self.da)*.10
        if self._basic>20000:
            self.tax=self._basic*.02
        else:
            self.tax=0
        self.net=self._basic+self.da+self.hra-self.tax
    def payslip_display(self):
        print("da:",self.da)
        print("hra:",self.hra)
        print("tax:",self.tax)
        print("net salary",self.net)
e=payslip()
e.emp_read()
e.calculation()
e.emp_display()
e.payslip_display()
