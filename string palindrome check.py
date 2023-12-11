string = input('enter the string to be checked for palindrome : ' ) 
reversed_string = string[::-1]
if(string == reversed_string):
    print('its a palindrome')
else :
    print('Its not a palindrome')
    