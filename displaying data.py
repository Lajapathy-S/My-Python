item = input('Enter the item name : ')
price = int(input('Enter the price of the item : '))
total_length = len(item) + len(str(price)) 
required_dots = 25 - total_length
print(item,required_dots * '.'  ,price )