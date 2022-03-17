"""
Core syntax in our Class design
In this we will look onto, how Python allows us to take advantage of operators in our classes.
Python is largely objects and methods call on objects and this even goes on even
when its hidden by some convenient syntax.
"""

var1 = 'Hello '
var2 = 'World!'
print(var1 + var2)

var3 = var1.__add__(var2)
print(var1)  # Hello
print(var3)  # Hello World

num1 = 45
num2 = 60
num3 = num1.__add__(num2)
print(num1)  # 45
print(num3)  # 105

var4 = ['a', 'b']
var5 = ['hello', 'John']
var6 = var4.__add__(var5)
print(var4)
print(var6)

"""
So if we have to add magic method     add     to our own classes, could we do that too.
Let’s try to do that.
We have a class called Sumlist which has a contructor     init      which takes list as an
argument called my_list.
"""


class SumList(object):
    def __init__(self, my_list):
        self.mylist = my_list

    def __add__(self, other):
        new_list = [x + y for x, y in zip(self.mylist, other.mylist)]

        return SumList(new_list)

    def __repr__(self):
        return str(self.mylist)


aa = SumList([3, 6, 9, 12, 15])
bb = SumList([100, 200, 300, 400, 500])
cc = aa + bb  # cc = aa.__add__(bb)
print(cc)
cc = aa.__add__(bb)
print(aa)
print(cc)

"""
But there are many methods which are internally managed by others magic methods.
Below are some of them,
"""

'abc' in var1  # var1.__contains__('abc')

var1 == 'abc'  # var1.__eq__('abc')

var1[1]  # var1.__getitem__(1)

var1[1:3]  # var1.__getslice__(1, 3)

len(var1)  # var1.__len__()

print(var1)  # var1.__repr__()

