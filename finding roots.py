import math
a = int(input("Enter a = "))
b = int(input("Enter b = "))
c = int(input("Enter c = "))
r1 = (-b + math.sqrt (b**2 - 4*a*c))/(2*a)
r2 = (-b - math.sqrt (b**2 - 4*a*c))/(2*a)
print ("The root r1 = ",r1)
print ("The root r2 = ",r2)