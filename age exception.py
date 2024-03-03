age = int(input('Enter the age of the person :'))

class negativeexception(Exception) :
    pass

def stage (a):
    if a <0 :
        return 'invalid input'
        
    elif a >0 and a <= 13 :
        return 'kid'
    elif a>13 and a <=19 :
        return 'teen'
    elif a>19 and a <=50 :
        return 'young'
    else :
        return 'old'

try :
    d = stage(age)
    print(d)
except negativeexception as e:
    print(e)
   






    