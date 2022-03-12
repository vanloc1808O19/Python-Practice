class MyClass(object):
    classy = 'class value'

dd = MyClass()
print(dd.classy)  # this should return the string 'class value'

dd.classy = 'Instance value'
print(dd.classy)  # return the string 'Instance value'

# this will delete the value set for 'dd.classy' in the instance
del dd.classy

# since the overriding attribute was deleted,
# this will print 'class value'

print(dd.classy)  # 'class value'
