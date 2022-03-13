# file IO
text = 'This is the first line\n'
file = open('datawork.txt', 'w')
file.write(text)
file.close()

f = open('datawork.txt', 'a')
text1 = 'This is the second line'
f.write(text1)
f.close()

f = open('datawork.txt', 'r+')
print(f.readline())
print(f.read())
f.close()

# an alternative to method overloadding
class Human:
    def sayHello(self, name = None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello')


# create instance
obj = Human()

# call the method, else part will be executed
obj.sayHello()

# call the method with a parameter, if part will be executed
obj.sayHello('Loc')
