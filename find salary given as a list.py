list1 = [int(x) for x in input('Enter the working hours :').split()] 
rate = int(input('Entrer the hourly rate :'))
sum = 0 
for i in range (len(list1)) :
    sum = sum + list1[i]

sal = sum * rate
print('The salary is ',sal)

