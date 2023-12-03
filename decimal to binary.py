n = int(input ('Enter the number to be converted to binary : '))
r = 0
req = 0
p = 0
fin = 0
num = 0
while n>0 :
    r = n%2
    req = (p * 10 ) + r
    p = req
    n = n//2

num = req

while num>0 :
    r = num % 10
    fin = (p*10) + r
    p = fin
    num= num // 10




print(fin)


