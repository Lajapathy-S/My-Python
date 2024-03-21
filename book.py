a = input ('Enter the title of the book :')
b = input ('Enter the author of the book :')
c = int(input ('Enter the price of the book :'))
class book :
    def __init__(self,d,e,f):
        self.title =  d 
        self.author =  e
        self.price =  f
    def show_details(self) :
        print('The title of the book is : ',self.title)
        print('The author of the book is : ',self.author)
        print('The price of the book is : ',self.price)
z = book(a,b,c)
z.show_details()