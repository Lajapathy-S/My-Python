b = int(input('Enter the radius of the circle :'))
class circle :
    def __init__(self,r) :
        self.radius = r
    def area(self):
            return 3.14*self.radius*self.radius
    def perimeter(self) :
            return 2 * 3.14 * self.radius
    
    
a = circle(b)
print(a.area())
print(a.perimeter())