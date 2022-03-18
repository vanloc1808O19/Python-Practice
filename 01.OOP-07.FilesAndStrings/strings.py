"""
Strings  are  the  most  popular  data  types  used  in  every  programming  language.  Why?
Because we, understand text better than numbers, so in writing and talking we use text and words,
similarly in programming too we use strings. In string we parse text, analyse text semantics, and
do data mining – and all this data is human consumed text.
The string in Python is immutable.
"""

import datetime as dt

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

# string formatting
# basic formatting
print('{} {}'.format('Example', 'One'))
print('{} {}'.format('pie', '3.1415926'))
print('{1} {0}'.format('pie', '3.1415926'))

# padding and aligning strings
print('{:12} a'.format('Python'))
print('{:>12}'.format('Python'))
print('{:<{}s} a'.format('Python', 12))
print('{:*<12}'.format('Python'))
print('{:*^12}'.format('Python'))
print('{:.15}'.format('Python Object Oriented Programming'))
# above, truncate 15 characters from the left side of a specified string
print('{:.{}}'.format('Python Object Oriented Programming', 15))

# named placeholders
data = {'Name': 'Raghu', 'Place': 'Bangalore'}
print('{Name} {Place}'.format(**data))

# datetime

print('{:%Y/%m/%d.%H:%M}'.format(dt.datetime(2022, 3, 18, 11, 45)))

# strings are unicode
"""
Strings  as  collections  of  immutable  Unicode  characters.  Unicode  strings  provide  an 
opportunity to create software or programs that works everywhere because the Unicode strings can 
represent any possible character not just the ASCII characters.
Many IO operations only know how to deal with bytes, even if the bytes object refers to textual 
data. It is therefore very important to know how to interchange between bytes and
Unicode.
"""

# converting text to bytes
"""
Converting a strings to byte object is termed as encoding. There are numerous forms of encoding, 
most common ones are: PNG; JPEG, MP3, WAV, ASCII, UTF-8 etc. Also this(encoding)  is a format to 
represent audio, images, text, etc. in bytes.
This conversion is possible through encode(). It take encoding technique as argument.
By default, we use ‘UTF-8’ technique.
"""

# Python code to demonstrate string encoding
# initialize a string
x = 'Nguyen Van Loc'

# initialize a byte object
y = b'Nguyen Van Loc'

# using encode() to encode the string
# encoded version of x is stored in z using ASCII mapping
z = x.encode('ASCII')

# check if x is converted to bytes or not
if z == y:
    print('Encode successfully')
else:
    print('Encode unsuccessfully')

# converting bytes to text
"""
Converting bytes to text is called the decoding. This is implemented through decode(). We can 
convert a byte string to a character string if we know which encoding is used to encode it.
So Encoding and decoding are inverse processes.
"""

# Python code to demonstrate byte decoding
# initialize a string
x = 'Nguyen Van Loc'

# initialize a byte object
y = b'Nguyen Van Loc'

# using decode() to decode the byte object
# decoded version of y is stored in z using ASCII mapping
z = y.decode()

# check if y is converted to string or not
if z == x:
    print('Decode successfully')
else:
    print('Decode unsuccessfully')