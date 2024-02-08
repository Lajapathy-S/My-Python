list1=[str(x) for x in input('Enter the list of words for the analysis:').split()]
s = input('Enter the first letter of the word present in the list to be found :')
counter = 0 
res =''
for i in list1 :
     for j in i :
          if (counter == 0 and s==j ) :
               res = i 
               counter = counter + 1
          else :
               counter = counter + 1 
        

print (res)
     
