balance = 10000 
n = int(input('Enter the amount to be withdrawn : '))
class balanceexception(Exception) :
    pass 

def withdraw(a):
    r = balance - a
    if r >= 5000 :
        print('The balance is ', r)
    else :
        print( 'The balance is less than 5000')

try :
   a= withdraw (n)
except balanceexception as e :
    print (e)


