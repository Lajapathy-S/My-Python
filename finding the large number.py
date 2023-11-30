n = int(input('Enter the number of items to be added : '))
count = 0 

max = 0
p = 0

while count<n :
    temp = int(input('enter the number : '))
    if temp > p :
        max = temp
    else :
        max = p
    p = max
    count = count +1
print('the max is :',max)






