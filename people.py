from PrintOut import print_words

class Person:

    def __init__(self, name, saying):
        self.name = name
        self.saying = saying

    def speak(self):
        print_words('My name is ' + self.name)
        print_words(self.saying)

