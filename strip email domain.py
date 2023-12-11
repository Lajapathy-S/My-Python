email = input('Enter the email : ')
at = email.find('@')
user_id = email[0:at]
domain = email[at+1 : len(email)]
print('The user id is : ',user_id)
print('the domain is :',domain)