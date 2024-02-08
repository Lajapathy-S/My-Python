list1 = [int(x) for x in input('Enter the numerical list1 item with space :').split()] 
list2 = [int(x) for x in input('Enter the numerical list2 item with space :').split()] 
list3=[]
for i in list1 : 
    for j in list2 : 
        if i == j :
            
            list3.append(i)
        else :
            pass

print('The item which is present in both the list are ',list3)



