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

