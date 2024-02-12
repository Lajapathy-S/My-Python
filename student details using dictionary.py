i = 0
main = {}
while i< 4 :
    s = {}
    temp = {}
    name = input('Enter the name of the student')
    age =  input('Enter the age of the student')
    roll_no = input('Enter the Rollno of the student')
    s['name'] = name
    s['age'] = age
    s['roll_no'] = roll_no
    temp[name] = s
    main.update(temp)
    i = i +1 

print(main)

