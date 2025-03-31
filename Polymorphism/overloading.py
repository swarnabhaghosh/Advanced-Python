#function overloading
class show:
    def draw(self,a=None,b=None):
        print("")
        if a!=None and b==None:
            ln=len(a)
            for i in range(1,ln+1):
                for k in range(ln-i+1):
                    print(" ",end="")
                for i in range(i):
                    print(a[i],end=" ")
                print(" ")
        elif a!=None and b!=None:
            for i in range(1,int(a)+1):
                for k in range(int(a)-i+1):
                    print(" ",end="")
                for j in range(1,2*i):
                    print(b,end="")
                print(" ")
        else:
            a=input("enter:")
            for i in range(1,int(a)+1):
                for k in range(int(a)-i+1):
                    print(" ",end="")
                for j in range(1,2*i):
                    print("*",end="")
                print(" ")
        
        
z1=show()
z1.draw('india')
z1.draw(3,'k')
z1.draw()

