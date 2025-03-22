class polygon:
      def __init__(self,l,b=None):
            self.l=l
            self.b=b
      def calc(self):
            raise NotImplementedError ("subclass must implement abstact method")
      def disp(self):
            raise NotImplementedError ("subclass must implement abstact method")

class rectangle(polygon):
      def calc(self):
            self.p=2*(self.l+self.b)
            self.a=(self.l*self.b)
      def disp(self):
            print("area of ractangle:",self.a)
            print("perimeter of ractangle:",self.p)

class square(polygon):
      def calc(self):
            self.p=4*(self.l)
            self.a=(self.l**2)
      def disp(self):
            print("area of square:",self.a)
            print("perimeter of square:",self.p)


poly1=rectangle(10,20)
poly2=square(10)
poly1.calc()
poly2.calc()
poly1.disp()
poly2.disp()
