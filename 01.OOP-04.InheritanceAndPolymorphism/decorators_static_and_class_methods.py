"""
    Functions(or methods) are created by def statement.
    Though methods works in exactly the same way as a function except one point where
    method first argument is instance object.
"""

"""
Simple  method:  defined  outside  of  a  class.  This  function  can  access  class
attributes by feeding instance argument:
"""

"""
def outside_func():
    pass


class A:
    Instance method
    def func(self,):
        pass

    class method: if we need to use class attributes
    @classmethod
    def cfunc(cls,):
        pass


    static method: do not have any info about the class
    @staticmethod
    def sfoo():
"""

"""
    Class method: 
    The @classmethod decorator, is a builtin function decorator that gets passed the class it was 
    called on or the class of the instance it was called on as first argument. The result of
    that evaluation shadows your function definition.
"""


class C(object):
    @classmethod
    def func(cls, arg1, arg2):
        pass

    # fun: function that needs to be converted into a class method
    # returns a class method for function

    """      
    They have the access to this cls argument, it can’t modify object instance state.
    That would require access to self.
    It is bound to the class and not the object of the class. 
    Class methods can still modify class state that applies across all instances of the class.
    """


"""
    Static method:
    A static method takes neither a self nor a cls(class) parameter but it’s free to accept an
    arbitrary number of other parameters
"""


class B(object):
    @staticmethod
    def fun(arg1, arg2):
        pass

    # A static method can neither modify object state nor class state.
    # They are restricted in what data they can access.

    """     
    When to use what
    •     We generally use class method to create factory methods. Factory methods return
    class object (similar to a constructor) for different use cases.
    •     We generally use static methods to create utility functions.
    """
