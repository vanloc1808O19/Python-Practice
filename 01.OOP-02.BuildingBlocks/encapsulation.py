class MyClass(object):
    def setAge(self, num):
        self.age = num

    def getAge(self):
        return self.age

zack = MyClass()
zack.setAge(45)
print(zack.getAge())

zack.setAge("Forty-five")
print(zack.getAge())