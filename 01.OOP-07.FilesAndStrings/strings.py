"""
Strings  are  the  most  popular  data  types  used  in  every  programming  language.  Why?
Because we, understand text better than numbers, so in writing and talking we use text and words,
similarly in programming too we use strings. In string we parse text, analyse text semantics, and
do data mining – and all this data is human consumed text.
The string in Python is immutable.
"""

# string manipulation
# string examples
a = "hello"
b = '''A multi line string, 
Simple!'''
e = ('multiple', 'strings', 'togethers')
print(a)
print(b)
print(e)

"""
String  manipulation  is  very  useful  and  very  widely  used  in  every  language.  Often, 
programmers are required to break down strings and examine them closely.
Strings can be iterated over (character by character), sliced, or concatenated. The syntax is the 
same as for lists.
The str class has numerous methods on it to make manipulating strings easier. The dir and help 
commands provides guidance in the Python interpreter how to use them.
Below are some of the commonly used string methods we use.
"""
str1 = 'Hello World!'
print(str1.startswith('h'))
print(str1.startswith('H'))
print(str1.endswith('d'))
print(str1.endswith('d!'))

print(str1.find('o'))

# above return the index of the first occurrence of the character/string
print(str1.find('lo'))

print(str1.upper())
print(str1.lower())

s = ('Hello! How are you?')
s1 = s.split(' ')
s2 = '*'.join(s1)
print(s2)

print(s.partition(' '))

