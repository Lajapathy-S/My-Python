n = input('Enter the expression to be evaluated :')


class evaluateexception(Exception):
    pass 

def evaluate(a) :
    s = (a.split())
    if len(s) < 3 :
        raise evaluateexception('Formula should have spaces like 10 + 5')
    if s[1] == '+' :
        print ('The sum is : ',int(s[0])+int(s[2]))
    elif s[1] == '-' :
        print ('The sum is : ',int(s[0])-int(s[2]))
    elif s[1] == '*' :
        print ('The sum is : ',int(s[0])*int(s[2]))
    elif s[1] == '/' :
        print ('The sum is : ',int(s[0])/int(s[2]))
    else :
        print ('The expression is invalid')

try:
    evaluate(n)
except evaluateexception as e :
    print (e)




