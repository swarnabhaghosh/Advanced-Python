class employee:
    def __init__(self,s1=None,s2=None,s3=None):
        self.id=s1
        self.name=s2
        self.basic=s3
    def employee_read(self):
        self.id=int(input("\nenter employee ID:"))
        self.name=input("enter employee name:")
        self.basic=int(input("enter basic salary:"))
    def employee_display(self):
        print("employee ID:",self.id)
        print("name:",self.name)
        print("basic:",self.basic)

class department:
    def __init__(self,s4=None,s5=None):
        self.dname=s4
        self.dadd=s5
    def department_read(self):
        self.dname=input("enter department:")
        self.dadd=input("enter department address:")
    def department_disp(self):
        print("department:",self.dname)
        print("department address:",self.dadd)

class payslip(employee,department):
    def __init__(self,a=None,b=None,c=None,d=None,e=None):
        super().__init__(a,b,c)
        super(employee,self).__init__(d,e)
    def payslip_calc(self):
        self.da=self.basic*.40
        self.hra=self.basic*.10
        self.pf=self.basic*0.12
        self.net=self.basic+self.da+self.hra-self.pf
    def payslip_display(self):
        print("DA:",self.da)
        print("HRA:",self.hra)
        print("PF:",self.pf)
        print("Net salary:",self.net)
s=payslip()
s.employee_read()
s.department_read()
s.payslip_calc()
print()

s.employee_display()
s.department_disp()
s.payslip_display()

s1=payslip(2,"ratan",15000,"accounts","kolkata")
s1.employee_read()
s1.department_read()
s1.payslip_calc()
print()
s1.employee_display()
s1.department_disp()
s1.payslip_display()


    


