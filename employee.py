a = input ('Enter the name of the employee :')
b = input ('Enter the salary of the employee :')
c = input ('Enter the designation of the employee :')
class employee :
    counter = 100
    def __init__(self,d,e,f):
        self.name =  d 
        self.salary =  e
        self.designation =  f
        employee.counter = employee.counter + 1 
        
    def show_details(self) :
        print('The name of the employee is : ',self.name )
        print('The salary of the employee is : ',self.salary)
        print('The designation of the employee is : ',self.designation)
        print('The employee_id is : ',employee.counter)

z = employee(a,b,c)
z.show_details()
employee_count = employee.counter - 100
print ('The total employee in the organisation is  ',employee_count)