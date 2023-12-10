pass1 = str(input('Enter the password : '))
pass2 = str(input ('confirm the password : '))
if (pass1 == pass2) :
    print ('Both passwords are same')
elif (pass1.casefold() == pass2.casefold()) :
    print('kindly check the typecase')
else :
    print('Both passwords didnot match')