n = int(input('Enter the number of items to be added : '))
count = 0 

sum_positive = 0
sum_negative = 0
p = 0
neg = 0

while count<n :
    temp = int(input('enter the number : '))
    if temp > 0 :
         sum_positive = p + temp
         p = sum_positive
    else : 
          sum_negative = neg + temp
          neg = sum_negative

    count = count +1
print('the total positive sum is :',sum_positive)
print('the total negative sum is :',sum_negative)





