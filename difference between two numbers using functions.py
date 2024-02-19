c = int(input('Enter the first biggest number: '))
d = int(input('Enter the second lowest number: '))

def diff(a,b) :
    if (a-b) <= 5 :
        return True
    else :
        return False

e = diff(c,d)
print('The input number is less than or equal to 5 :',e) 

    
