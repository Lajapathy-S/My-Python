Birthday = {'sid':'20-10-1994','abishek':'26-06-95','ajith' : '12-06-1995'}
name= input('Enter the name of the person :')
result = Birthday.get(name,'entered name is not found in the dictionary')
print('The date of birth of the entered person is : ',result )
