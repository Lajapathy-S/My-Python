a = input('Enter the string to be checked for panagram : ')
def panagram (str) :
    all = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    phr = set(str)
    if phr.difference(all) == {' '} :
        return True
    else :
        return False 

res = panagram(a)

print('The provided string panagram result is :',res)