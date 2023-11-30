n = int(input('Enter a number to be reversed : '))
p = 0 
req = 0

while n > 0 :
    r = n % 10 
    req = (p * 10 )+ r
    p = req
    n = n // 10 
    
print (req)
