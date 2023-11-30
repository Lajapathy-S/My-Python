n = int(input('Enter the number of items to be added : '))
count = 0 

sum = 0
p = 0

while count<n :
    temp = int(input('enter the number : '))
    sum = p + temp
    p = sum
    count = count +1
print('the total sum is :',sum)






