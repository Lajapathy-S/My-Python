class course :
    def __init__(self,name,duration,*books):
        self.name = name
        self.duration = duration 
        self.books = [self.book(b) for b in books]

    def show_details(self) :
        print('The name of the course is :',self.name)
        print('The duration of the course is :',self.duration)
        print('The suggested books :')
        for b in self.books :
            print(b)

    class book :
        def __init__(self,title):
            self.title = title
        def __str__(self) :
            return self.title

c1 = course('programming in python','10 months','learn python','python made easy')
c1.show_details()