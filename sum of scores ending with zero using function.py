lst1 = [int(x) for x in input('Enter the marks seperated by space :').split() ]
def summation (a) :
    sum = 0
    for i in a :
        if i % 10 == 0 :
            sum = sum + i
        else :
            pass 
    return sum

ans = summation(lst1)
print ("The summaiton of marks ending with zero is : ",ans)
