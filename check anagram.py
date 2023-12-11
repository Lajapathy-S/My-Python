string_1= input('Enter the first input : ')
string_2= input('Enter the second input to be checked for anagram : ')

count = 0
for i in string_1 :
    #a = i
    if string_2.find('i') > 0 :
        count = count + 1 


if count == len(string_2) :
     print ('Its a anagram')
else :
     print('its not a anagram')




