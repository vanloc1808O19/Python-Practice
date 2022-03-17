"""
Inherit from built-in types
Classes can also inherit from built-in types this means inherits from any built-in and take
advantage of all the functionality found there.

In below example we are inheriting from dictionary but then we are implementing one of its  method
    setitem__.  This  (setitem)  is  invoked  when  we  set  key  and  value  in  the
dictionary. As this is a magic method, this will be called implicitly.
"""


class MyDict(dict):
    def __setitem__(self, key, value):
        print('Setting a key and value!')
        dict.__setitem__(self, key, value)


dd = MyDict()
dd['a'] = 10
dd['b'] = 20

for key in dd.keys():
    print('{0} = {1}'.format(key, dd[key]))

"""
Let’s  extend  our  previous  example,  below  we  have  called  two  magic  methods  called
    getitem     and     setitem     better invoked when we deal with list index.
"""

# mylist inherits from 'list' object but indexes from 1 instead of 0
class Mylist(list):  # inherits from list
    def __getitem__(self, index):
        if index <= 0:
            raise IndexError
        else:
            index -= 1
            return list.__getitem__(self, index)    # this method is called when
                                                    # we access a value with subscript like x[1]

    def __setitem__(self, index, value):
        if (index <= 0):
            raise IndexError
        else:
            list.__setitem__(self, index, value)


x = Mylist(['a', 'b', 'c'])  # __init__() inherited from built-in list

print(x)  # __repr__() inherited from built-in list

x.append('HELLO')  # append() inherited from built-in list

print(x[1])
print(x[4])
