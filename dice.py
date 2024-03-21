from random  import *
class dice :
     
     def __init__(self,sides) :
         self.sides = sides 

     def rolldice (self) :
          return randint(1,self.sides)
     
c= dice(6)
print(c.rolldice())

     
          

