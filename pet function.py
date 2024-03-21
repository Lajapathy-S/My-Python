class cat :
    def __init__(self,name,age) :
        self.name = name 
        self.age = age 
    def info(self) :
         print('The name of the cat is :',self.name)
         print('The age of the cat is :',self.age)
    def make_sound(self) :
        print('The sound of the cat is meow')

class dog :
    def __init__(self,name,age) :
        self.name = name 
        self.age = age 
    def info(self) :
         print('The name of the dog is :',self.name)
         print('The age of the dog is :',self.age)
    def make_sound(self) :
        print('The sound of the dog is lol lol')

def mypet(pet) :
    pet.info()
    pet.make_sound()

c = cat('micky','2')
d = dog('rot','12')
mypet(c)
mypet(d)