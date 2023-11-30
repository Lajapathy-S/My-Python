n = int(input('Enter the number : '))
count = 0 
sum = 0
r = 0
while n >0 :
    r = n % 10 
    sum = sum + r
    n = n // 10 

print ('sum of the digits of the number is ',sum)

