class person:
      def __init__(self,name,age):
            self.name=name
            self.age=age
      def show(self):
            print("name:",self.name)
            print("age:",self.age)
class student(person):
      def __init__(self,name,age,rollno,marks):
            super().__init__(name,age)
            self.rollno=rollno
            self.marks=marks
      def show(self):
            super().show()
            print("Roll no:",self.rollno)
            print("Marks:",self.marks)

s=student("ram",18,10,55)
s.show()
      
