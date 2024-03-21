class customer :
    def __init__ (self,n,ph) :
        self.name = n
        self.phone = ph
    def getname(self):
        return self.name
    def getphone(self):
        return self.phone
    def setphone(self,l):
        self.phone = l

a = customer('laja','105')
print(a.getname())
print(a.getphone())
a.setphone(106)
print(a.getphone())

        