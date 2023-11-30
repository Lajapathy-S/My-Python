n = int(input('Enter a number to be checked for palindrome : '))
num = n
p = 0 
req = 0

while n > 0 :
    r = n % 10 
    req = (p * 10 )+ r
    p = req
    n = n // 10 
    
if num == req :
    print('The Entered number is a palindrome')
else :
    print('The Entered number is not a palindrome')


