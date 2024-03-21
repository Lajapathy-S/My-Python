import math
a = int(input('Enter the number of sides in the polygon: ' ))
b = [int(item) for item in input('Enter the sides with spaces : ').split()]
class polygon :
    def __init__(self,ns,*sides) :
        self.numberofsides = ns
        self.sidevalues = sides

class triangle(polygon) :
    def _init__(self,ns,*sides) :
        polygon.__init__(self,ns,*sides) 
      
    
    def area(self) :
        y = self.sidevalues
       
        s = (sum(y))/2
        r = 1
        for m in self.sidevalues :
            v = r * (s-m)
            r = v 

        area = math.sqrt(s*r)
        return area

t1  = triangle(a,b)
print(t1.area())
    

    






            



