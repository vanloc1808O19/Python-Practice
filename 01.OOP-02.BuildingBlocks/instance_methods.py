class MyClass(object):
    var = 9

    def firstM(self):
        print("Hello, World!")
        print(self)

obj = MyClass()
print(obj.var)
obj.firstM()
print(obj)
