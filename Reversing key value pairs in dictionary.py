dict1  = {'1':'a' ,'2':'b'}
def reverse (c) :
    res = {}
    for x in (c) :
        values = c.get(x)
        res[values] = x
    
    return res

res1 = reverse(dict1)
print ('The reversed dictionary input is :',res1)
