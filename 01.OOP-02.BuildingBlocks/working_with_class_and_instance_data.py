class InstanceCounter(object):
    count = 0  # class attribute, will be accessible to all instances

    def __init__(self, val):
        self.val = val

        InstanceCounter.count += 1  # increase the value of class attribute,
        # accessible through class name

    # in above lines, class ('InstanceCounter') act as an object

    def set_val(self, new_val):
        self.val = new_val

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count


a = InstanceCounter(9)
b = InstanceCounter(18)
c = InstanceCounter(27)

for obj in (a, b, c):
    print('val of obj: %s' % (obj.get_val()))  # initialized value (9, 18, 27)

    print('count: %s' % (obj.get_count()))  # always 3


class MyClass:
    class_attribute = 99

    def __init__(self):
        self.instance_attribute = None

    def class_method(self):
        self.instance_attribute = 'I am instance attribute'


print(MyClass.__dict__)

a = MyClass()
a.class_method()
print(a.__dict__)
