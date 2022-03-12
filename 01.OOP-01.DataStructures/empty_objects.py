# empty objects

obj = object()
obj.x = 9
"""
    Traceback (most recent call last):
  File "F:\GitHub\Python-Practice\01.OOP-01.DataStructures\empty_objects.py", line 3, in <module>
    obj.x = 9
AttributeError: 'object' object has no attribute 'x'
"""

class EmpObject:

obj = EmpObject()
obj.x = "Hello World"
print(obj.x)
# not work?