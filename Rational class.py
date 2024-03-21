class rational :
    def __init__(self,p,q):
        self.p = p
        self.q = q
    
    def __add__(self,other) :
        s = rational(self.p,self.q) 
        s.p = (self.p * other.q) + (self.q * other.p)
        s.q = self.q * self.q
        return s 
    def __sub__(self,other) :
        s = rational(self.p,self.q) 
        s.p = (self.p * other.q) - (self.q * other.p)
        s.q = self.q * self.q
        return s 
    def __str__(self) :
        return str(self.p) +'/'+str(self.q)

c1 = rational (4,5)
c2 = rational (4,5)
c3 = c1 - c2 
print (c3)