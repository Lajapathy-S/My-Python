class orders :
    def __init__(self,*cart):
        self.cart = []
    def add_to_items(self,name):
         self.cart.append(name)
    def remove_items(self,name):
         self.cart.remove(name)
    def __len__(self):
        return len(self.cart)
    def __str__(self):
        items = 'cart contains : '
        for a in self.cart :
            items += a +' ,'
        
        return items
c = orders()
c.add_to_items('laja')
c.add_to_items('sid')
c.add_to_items('abishek')
print('length of cart ' ,len(c))
print(c)