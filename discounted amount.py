amount = float(input("Enter the amount"))
discount = 0
if amount <= 1000 :
    discount = 10
elif amount > 1000 and amount <= 5000 :
    discount = 20
elif amount > 5000 and amount <= 10000 :
    discount = 30
else :
    discount = 50 
discounted_amt = ((100-discount)/100)*amount
print("The discounted amount is ",discounted_amt)
