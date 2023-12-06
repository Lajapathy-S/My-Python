a = int(input("Enter the start number of the series : "))
d = int(input("Enter the difference of the series : "))
n = int(input("Enter the number of terms in the series : "))

for r in range(a, a+(n*d), d) :
   print(r)


