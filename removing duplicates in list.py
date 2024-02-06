list1 = [int(x) for x in input('Enter the numbers with space :').split()] 
list2 = []
for i in list1 :
    if i not in list2 :
        list2.append(i)
    else :
        pass 
print(list2)


