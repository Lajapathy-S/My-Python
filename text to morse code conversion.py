codes = ['._','_...','_._.','_..','.','.._.','__.','....','..','.___']
str1 = input('Enter a lowercase string which has characters below j :')
req = 0
list1 = []
temp=''
for i in str1 :
    req = ord(i) - ord('a')
    temp = codes[req]
    list1.append(temp)
    
print(list1)
