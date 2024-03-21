a = int(input('Enter the first variable :'))
b = int(input('Enter the second variable :'))

class calculator :

    @staticmethod

    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
    def division(x,y):
        return x/y
    def multiply(x,y):
         return x*y

print ('The sum is :',calculator.add(a,b))
print ('The sub is :',calculator.sub(a,b))
print ('The multiplication is :',calculator.multiply(a,b))
print ('The division is :',calculator.division(a,b))