"""
Overview:
Modern software development needs to address complex business requirements. It also needs to take
into account factors such as future extensibility and maintainability. A good design of a software
system is vital to accomplish these goals. Design patterns play an important role in such systems.
To understand design pattern, let’s consider below example-
•     Every car’s design follows a basic design pattern, four wheels, steering wheel, the core
drive system like accelerator-break-clutch, etc.
So, all things repeatedly built/ produced, shall inevitably follow a pattern in its design.. it
cars, bicycle, pizza, atm machines, whatever…even your sofa bed.
Designs     that     have     almost     become     standard     way     of     coding     some
logic/mechanism/technique  in  software,  hence  come  to  be  known  as  or  studied  as,
ware Design Patterns.
"""


"""
Why is Design Pattern Important?
Benefits of using Design Patterns are:
•     Helps you to solve common design problems through a proven approach
•     No ambiguity in the understanding as they are well documented.
•     Reduce the overall development time.
•     Helps  you  deal  with  future  extensions  and  modifications  with  more  ease  than
otherwise.
•     May  reduce  errors  in  the  system  since  they  are  proven  solutions  to  common
problems.
"""


""""
Classification of Design Patterns
The  GoF  (Gang  of  Four)  design  patterns  are  classified  into  three  categories  namely
creational, structural and behavioral.

Creational Patterns
Creational design patterns separate the object creation logic from the rest of the system. Instead 
of you creating objects, creational patterns creates them for you. The creational patterns include 
Abstract Factory, Builder, Factory Method, Prototype and Singleton.
Creational Patterns are not commonly used in Python because of the dynamic nature of the language. 
Also language itself provide us with all the flexibility we need to create in a sufficient elegant 
fashion, we rarely need to implement anything on top, like singleton or Factory.
Also these patterns provide a way to create objects while hiding the creation logic, rather
than instantiating objects directly using a new operator.

Structural Patterns
Sometimes instead of starting from scratch, you need to build larger structures by using an 
existing set of classes. That’s where structural class patterns use inheritance to build a new 
structure. Structural object patterns use composition/ aggregation to obtain a new functionality. 
Adapter,  Bridge, Composite, Decorator, Façade, Flyweight  and  Proxy  are Structural Patterns. 
They offers best ways to organize class hierarchy.

Behavioral Patterns
Behavioral patterns offers best ways of handling communication between objects. Patterns comes 
under this categories are: Visitor, Chain of responsibility, Command, Interpreter, Iterator,  
Mediator,  Memento,  Observer,  State,  Strategy  and  Template  method  are Behavioral Patterns.
Because they represent the behavior of a system, they are used generally to describe the
functionality of software systems.
"""


"""
Commonly used Design Patterns
Singleton
It is one of the most controversial and famous of all design patterns. It is used in overly 
object-oriented languages, and is a vital part of traditional object-oriented programming.
The Singleton pattern is used for,
•     When logging needs to be implemented. The logger instance is shared by all the components of 
the system.
•     The  configuration  files  is  using  this  because  cache  of  information  needs  to  be 
maintained and shared by all the various components in the system.
•     Managing a connection to a database.

"""


class Logger(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)

        return cls._logger


obj1 = Logger()
obj2 = Logger()
print(obj1 == obj2)

print(obj1)
print(obj2)
