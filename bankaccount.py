a = input('Enter the name of the account holder:')
b = int(input('Enter the balance of the account holder(above 1000) :'))

class minimumbalanceerror(Exception) :
    pass 

class account :
    accountno = 1000
    def __init__(self,c,d = 1000) :
        if d < 1000 :
            raise minimumbalanceerror('Account cant be created')
        self.name = c
        self.balance = d
        self.accountnum = account.accountno
        account.accountno = account.accountno + 1
    def deposit(self,e) :
        return int(self.balance) + int(e)
    def withdraw(self,f) :
        self.balance = int(self.balance) - int(f )
        if self.balance < 1000 :
            raise minimumbalanceerror('Account cant be withdrawn')
        else :
            pass
    def show_details(self):
        print('The name of the account holder is :', self.name)
        print("The balance of the account holder is :",self.balance)
        print('The account holders number is ',self.accountnum)

g = account(a,b)
g.show_details()

h = account('raj',2200)
h.show_details()

h.withdraw('500')
h.show_details()

h.withdraw('1000')
h.show_details
        
    
        
    
