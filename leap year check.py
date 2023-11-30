year = int(input("Enter the year "))
if year%400 == 0 and year%100 == 0 :
    print("Entered year is leap year")
elif year%4 == 0 and year%100 != 0 :
    print ("Entered year is a leap year")
else :
    print ("Enrered year is not a leap year")