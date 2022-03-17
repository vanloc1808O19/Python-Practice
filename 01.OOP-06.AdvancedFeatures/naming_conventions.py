"""
Naming conventions

In this we will look into names we’ll used for variables especially private variables and
conventions used by Python programmers worldwide. Although variables are designated as  private
but  there  is  not  privacy  in  Python  and  this  by  design.  Like  any  other  well documented
languages, Python has naming and style conventions that it promote although it doesn’t  enforce
them. There is a style guide written by  “Guido  van  Rossum”  the originator of Python, that
describe the best practices and use of name  and is called PEP8. Here is the link for this,
https://www.Python.org/dev/peps/pep-0008/

PEP  stands  for  Python  enhancement  proposal  and  is  a  series  of  documentation  that
distributed among the Python community to discuss proposed changes. For example it is
recommended all,
•     Module names : all_lower_case
•     Class names and exception names: CamelCase
•     Global and local names: all_lower_case
•     Functions and method names: all_lower_case
•     Constants: ALL_UPPER_CASE
These are just the recommendation, you can vary if you like. But as most of the developers follows
these recommendation so might me your code is less readable.
Why conform to convention?
We can follow the PEP recommendation we it allows us to get,
•     More familiar to the vast majority of developers
•     Clearer to most readers of your code.
•     Will match style of other contributers who work on same code base.
•     Mark of a professional software developers
•     Everyone will accept you.

Variable Naming: ‘Public’ and ‘Private’
In Python, when we are dealing with modules and classes, we designate some variables or attribute
as private. In Python, there is no existence of “Private” instance variable which cannot be
accessed except inside an object. Private simply means they are simply not intended  to  be  used
by  the  users  of  the  code  instead  they  are  intended  to  be  used internally. In general, a
convention is being followed by most Python developers i.e. a name prefixed with an underscore for
example. _attrval (example below) should be treated as a non-public part of the API or any Python
code, whether it is a function, a method or a data member. Below is the naming convention we
follow,
•     Public attributes or variables (intended to be used by the importer of this module or user of
this class):          regular_lower_case
•     Private   attributes   or   variables   (internal   use   by   the   module   or   class):
_single_leading_underscore
•     Private attributes that shouldn’t be subclassed:        double_leading_underscore
•     Magic attributes:       double_underscores     (use them, don’t create them)
"""


class GetSet(object):
    instance_count = 0  # public

    __mangle_name = 'no privacy'  # special variable


