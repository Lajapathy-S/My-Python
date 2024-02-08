# list1 = [list(x) for x in input('Enter the first matrix elements seperated by space :').split()]
# list2 = [list(x) for x in input('Enter the second matrix elements of same size as first one seperated by space :').split()]
list1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
list2 = [[5,6,7,8],[5,6,7,8],[5,6,7,8],[5,6,7,8]]
temp = 0
list4 = []
for i in range(len(list1)) :
    s=[]
    for j in range (len(list1[0])) :
        temp = list1[i][j] + list2[i][j]
        s.append(temp)
    list4.append(s)

print (list4)
