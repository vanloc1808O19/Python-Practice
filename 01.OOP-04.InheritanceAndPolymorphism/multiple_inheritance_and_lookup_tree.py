"""
    As its name indicates, multiple inheritance in Python is when a class inherits from multiple
    classes.
"""

# Python multiple inheritance syntax
"""
    To make a class inherits from multiple parents classes, we write the the names of these classes 
    inside the parentheses to the derived class while defining it. We separate these
    names with comma.
"""


class Mother:
    pass


class Father:
    pass


class Child(Mother, Father):
    pass


print(issubclass(Child, Mother) and issubclass(Child, Father))


"""
    Multiple inheritance refers to the ability of inheriting from two or more than two class. The 
    complexity arises as child inherits from parent and parents inherits from the grandparent class. 
    Python climbs an inheriting tree looking for attributes that is being requested to be
    read from an object. It will check the in the instance, within class then parent class and 
    lastly from the grandparent class. Now the question arises in what order the 
    classes will be searched - breath-first or depth-first. By default, Python goes with the
    depth-first.
"""

# an example of mro feature of Python


class A(object):
    def do_this(self):
        print('Doing this in A')


class B(A):
    pass


class C(object):
    def do_this(self):
        print('Doing this in C')


class D(B, C):
    pass


d_instance = D()
d_instance.do_this()
print(D.mro())


# another example when 2 parents classes inherit from a grandparent


class A1(object):
    def do_this(self):
        print('Doing this in A1')


class B1(A1):
    pass


class C1(A1):
    def do_this(self):
        print('Doing this in C1')


class D1(B1, C1):
    pass


d1_instance = D1()
d1_instance.do_this()
print(D1.mro())

"""   
    Simple rule to understand the above output is- if the same class appear in the method resolution 
    order, the earlier appearances of this class will be remove from the method
    resolution order.
"""
