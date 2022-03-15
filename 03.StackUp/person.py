"""
    Step 1: Define a Class called Person
    Define a Class called Person that takes in two arguments - name and age.
    Your Person will need to be instantiated with the following attributes:
    - name
    - age
    - favorite_quotes (an empty list)
"""


class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
        self.favorite_quotes = []

    def say_hello(self):
        print("Hello World")

    def say_name(self):
        print("My name is {0}".format(self.name))

    def say_age(self):
        print("I was born in {0}".format(2022 - self.age))

    def add_quote(self, s):
        self.favorite_quotes.append(s)

    def count_quotes(self):
        print("I have {0} quotes in me".format(len(self.favorite_quotes)))


stackup_test = Person("John", 21)

stackup_test.say_hello()

stackup_test.say_name()

stackup_test.say_age()

stackup_test.add_quote("This is quote 1")

stackup_test.add_quote("This is quote 2")

stackup_test.count_quotes()
