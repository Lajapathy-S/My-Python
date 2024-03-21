a = input('Enter the name of te currency :')
b = input('Enter the rate /value of that currency :')
g =input ('Enter the total currency to be converted :')

class currency :
    def __init__ (self,c,d) :
        self.name = c
        self.rate = d
    def getcurrencyname(self):
        return self.name 
    def setcurrencyname(self,e):
         self.name = e
    def getcurrencyrate(self):
        return self.rate 
    def setcurrencyrate(self,f):
         self.rate = f
    def converter(self,amount) :
         return int(self.rate) * int(amount)

cc = currency(a,b)

print('The converted amount is ',cc.converter(g))

         
         
        