a = input('Enter the string to be checked : ')

def count (r) :
    uppercase = 0
    lowercase = 0 
    for i in r :
        if ord(i) >= 65 and ord(i) <= 90 :
            uppercase = uppercase + 1
        else :
            lowercase = lowercase + 1
    return uppercase,lowercase

u,v = count(a)

print ('The number of uppercase in the string is',u,'The number of lowercase in the string is ',v)

