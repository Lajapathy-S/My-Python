n = int(input("Enter the number to be checked for prime :"))
count = 0
for i in range(1,n+1) :
    if (n%i == 0) :
        count = count +1 

if count == 2 :
    print ("Its a prime number")
else :
    print("Its not a prime number")
