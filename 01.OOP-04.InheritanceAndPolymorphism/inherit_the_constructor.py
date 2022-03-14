# If we see from our previous inheritance example,     init     was located in the parent class in
# the up ‘cause the child class dog or cat did not ‘ve      init      method in it. Python used the
# inheritance attribute lookup to find     init     in animal class. When we created the child class,
# first it will look the      init      method in the dog class, then it did not find it then looked
# into parent class Animal and found there and called that there. So as our class design became
# complex we may wish to initialize a instance firstly processing it through parent
# class constructor and then through child class constructor.

import random as rd


class Animal(object):
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = rd.choice(['Doberman', 'German shepherd', 'Beagle'])

    def fetch(self, thing):
        print('{0} goes after the {1}!'.format(self.name, thing))


d = Dog('dog-name')

print(d.name)
print(d.breed)
