n=int(input("Enter the number for the multiplication table: "))
ans = 0
for i in range(1,11) :
    ans = n * i
    print (str(n)+"x"+str(i)+"="+str(ans))
