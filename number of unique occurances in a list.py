list1=[int(x) for x in input('Enter the list to be analysed for unique occurances :').split()]
counter = 0
list2 = []
for i in list1 :
    counter = list1.count(i)
    if i not in list2 :
        list2.extend([i,counter])
    else :
        pass


print ('The unique occurance in your provided list is',list2)