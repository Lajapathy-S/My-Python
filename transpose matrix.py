list1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
temp = 0
list4 = []
for i in range(len(list1[0])) :
    s=[]
    for j in range (len(list1)) :
        temp = list1[j][i]
        s.append(temp)
    list4.append(s)

print (list4)