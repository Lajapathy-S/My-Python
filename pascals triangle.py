n = int( input ('Enter the n value :'))
# r = int( input ('Enter the r value :'))

# def fact (a) :
#     if a == 0 :
#         return 1
#     else :
#         a = a * (fact(a - 1))
#         return a

# def pascal (u,v) :
#     for i in range(u):
#         l2 = []
#         for j in range(v):
#             num = fact(i)
#             den1 = fact(j-i) 
#             den2 = fact (j)
#             den = den1 * den2
#             res = num / den
#             l2.append (res)
#         print (l2)

def  pascall(l) :
    r = [1]
    for i in range(l) :
        print(r)
        # ex = r.append(0)
        ex = r + [0]
        # new = r.insert(0,0)
        new = [0] + r
        nr = [x+y for x,y in zip(ex,new)]
        r = nr
        


 

pascall(n) 
