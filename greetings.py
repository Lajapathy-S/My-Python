class english() :
    def greetings() :
        print('Hello my child,Dont worry ! be happy!')

class french() :
    def greetings() :
        print('Bonjour')

def greet(language) :
    language.greetings()

greet(english)
greet(french)