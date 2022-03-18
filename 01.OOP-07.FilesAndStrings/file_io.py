"""
Operating systems represents files as a sequence of bytes, not text.
A file is a named location on disk to store related information. It is used to permanently store
data in your disk.
In Python, a file operation takes place in the following order.
•     Open a file
•     Read or write onto a file (operation).
•     Close the file.
Python wraps the incoming (or outgoing) stream of bytes with appropriate decode (or encode) calls
so we can deal directly with str objects.
Opening a file
Python has a built-in function open() to open a file. This will generate a file object, also
called a handle as it is used to read or modify the file accordingly.

For reading text from a file, we only need to pass the filename into the function. The file will be
opened for reading, and the bytes will be converted to text using the platform
default encoding
"""