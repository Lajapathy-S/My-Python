n = int(input("Enter the number to which the factotial to be found : "))
fact = 1
for count in range(1,n+1):
    fact = fact * count

print ("The factorial of the number",n,"is",fact)
