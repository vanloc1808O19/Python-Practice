# polymorphism example

class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        #  common method for both subclasses
        print('{0} eats {1}'.format(self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print('{0} goes after the {1}'.format(self.name, thing))

    def show_affection(self):
        print('{0} wags tail'.format(self.name))


class Cat(Animal):
    def swat_string(self):
        print('%s shreds the string!' % (self.name))

    def show_affection(self):
        print('{0} purrs'.format(self.name))


for a in (Dog('Rover'), Cat('Fluffy'), Cat('Precious'), Dog('Scout')):
    a.show_affection()

# Python itself have classes that are polymorphic. Example, the len() function can be used
# with multiple objects and all return the correct output based on the input parameter.

print(len('hello'))  # pass a string to the len() function
print(len([1, 2, 3]))  # pass a list of 3 elements
print(len(('x', 'y', 'z')))  # pass a tuple of 3 elements
print(len({'a': 9, 'b': 18}))  # pass a dictionary of 2 elements

# illustrate it further
print(dir('hello'))
print(dir([1, 2, 3]))
print(dir(('x', 'y', 'z')))
print(dir({'a': 9, 'b': 18}))
