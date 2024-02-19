a = int(input('Enter the first number: '))
b = int(input('Enter the second  number: '))
c = int(input('Enter the third number: '))

def large (c,d,e) :
    if c> d and c > e :
        return c 
    elif d> c and d > e :
        return d
    else :
        return c

res = large(a,b,c)
print ("The largest of the three numbers are :",res)
