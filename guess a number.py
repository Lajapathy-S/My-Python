import random 
n = random.randint(1,10)
guess = 0
while guess != n :
    guess = int (input("Enter a number"))
    if guess > n :
        print ("It is larger than the entered number")
    elif guess <n:
        print ("It is smaller than the entered number")
    else :
        print ("the number is ",n)
        
    


