class angle():
    def __init__ (self,degree):
        self.degree = degree
    def __add__(self,b) :
        sum = angle(self.degree + b.degree)
        return sum
    def __str__(self):
        return 'The resultant angle is '+str(self.degree)
                                          
c1 = angle(5)
c2 = angle(10)
c3 = c1 + c2

print(c3)
                        