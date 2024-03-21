class robot():
    def __init__(self,name):
        self.name = name
    def say_hi(self):
        print('Hi',self.name)

class policerobot(robot):
    def say_hi(self):
        print('Hi this is '+self.name+'.Im here to help you')

c = robot('sid')
c.say_hi()
d = policerobot('robocop')
d.say_hi()