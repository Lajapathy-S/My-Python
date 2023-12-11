string = input('Enter the string : ')
lower_string =''
upper_string =''
for i in string :
    if i.islower() :
        lower_string = lower_string + i
    else :
        upper_string = upper_string + i


req_output = lower_string + upper_string
print(req_output)




