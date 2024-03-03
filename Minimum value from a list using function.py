l = list(int(x) for x in input('Enter the numbers to be checked for minimum :').split())
m = int(input('Enter the limit value :'))

def minimum (*var,limit = None) :
    if limit is None :
        return min(var)
    else :
       l2 = [x for x in var if x >= limit]
       return min (l2)


res = minimum(l,limit=m)
print ('The min value is ',res)


    