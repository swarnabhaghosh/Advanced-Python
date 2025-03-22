class player:
    def __init__(self,a=None,b=None):
        self.pid=a
        self.pname=b
    def player_read(self):
        self.pid=int(input("Enter player ID:"))
        self.pname=input("Enter player name:")
    def player_disp(self):
        print("Player ID:",self.pid)
        print("Player name:",self.pname)
class batsman(player):
    def __init__(self,s1=None,s2=None,c=None):
        super().__init__(s1,s2)
        self.runs=c
    def batsman_read(self):
        self.runs=int(input("Enter total runs:"))
    def batsman_disp(self):
        print("Total runs:",self.runs)
class bowler(player):
    def __init__(self,s1=None,s2=None,d=None):
        super().__init__(s1,s2)
        self.wickets=d
    def bowler_read(self):
        self.wickets=int(input("Enter total wickets:"))
    def bowler_disp(self):
        print("Total wickets:",self.wickets)
class allrounder(batsman,bowler):
    def __init__(self,s1=None,s2=None,s3=None,s4=None,e=None):
        super().__init__(s1,s2,s3)
        super(batsman,self).__init__(s1,s2,s4)
        self.bat_avg=e
    def allrounder_read(self):
        self.bat_avg=float(input("Enter batting average:"))
    def allrounder_disp(self):
        print("Batting average:",self.bat_avg)

'''
x=allrounder()
x.player_read()
x.batsman_read()
x.bowler_read()
x.allrounder_read()
print()
x.player_disp()
x.batsman_disp()
x.bowler_disp()
x.allrounder_disp()
'''

y=allrounder(10,"Sachin",25000,134,45.87)
y.player_disp()
y.batsman_disp()
y.bowler_disp()
y.allrounder_disp()




