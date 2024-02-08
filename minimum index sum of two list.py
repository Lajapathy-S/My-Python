list1 = [str(x) for x in input('Enter the favourite item with space :').split()] 
list2 = [str(x) for x in input('Enter the favourite item with space :').split()] 
sum = 0
list3=[]
for i in list1 : 
    for j in list2 : 
        if i == j :
            sum = list1.index(i) + list2.index(j)
            list3.append(sum)
        else :
            pass

low = min(list3)
string1  = list3.index(low)
print('The favourite item with minimum index for both is ',list1[string1])
# print(low)


