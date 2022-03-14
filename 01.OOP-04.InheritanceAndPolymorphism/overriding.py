# In Python, when a subclass contains a method that overrides a method of the superclass,
# you can also call the superclass method by calling
# super(Subclass, self.method  instead of self.method.

class Thought(object):
    def __init__(self):
        print('Thought')

    def message(self):
        print("Thought, always come and go")


class Advice(Thought):
    def __init__(self):
        super(Advice, self).__init__()
        print('Advice')

    def message(self):
        print('Warning: Risk is always involved when you are dealing with market')


a = Advice()

