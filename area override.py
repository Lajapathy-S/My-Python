import math 

class shape :
    def __init__ (self,name):
        self.name = name 
    def area() :
        pass

class rectangle(shape):
    def __init__(self,l,b) :
        self.length = l
        self.breadth = b
    def area (self):
        return self.length * self.breadth

class circle (shape):
    def __init__(self,radius) :
        self.radius = radius
    def area(self) :
        return math.pi * self.radius * self.radius

r = rectangle(5,10)
print('The area of the triangle',r.area())
c = circle (5)
print ('The area of the triangle',c.area())
    
    