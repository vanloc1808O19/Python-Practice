# inheritance example
class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        # common method for both subclasses
        print('% s is eating %s.' % (self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print('%s goes after the %s!' % (self.name, thing))


class Cat(Animal):
    def swat_string(self):
        print('%s shreds the string!' % (self.name))


d = Dog('Ranger')
c = Cat('MeOw')

d.fetch('ball')
c.swat_string()

d.eat('dog food')
c.eat('cat food')

# d.swat_string() -> error
