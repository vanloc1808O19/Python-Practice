# define dictionaries

# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict1 = {1: 'msft', 2: 'IT'}

# dictionary with mixed keys
my_dict2 = {'name': 'Aarav', 1: [2, 4, 6, 8, 10]}

# using built-in function dict()
my_dict3 = dict({1: 'msft', 2: 'IT'})

# from sequence having each item as a pair
my_dict4 = dict([(1, 'msft'), (2, 'IT')])

# access elements of dictionary
print(my_dict1[1])
print(my_dict1[2])
# print(my_dict['IT'])  # error


# modify dictionaries
my_dict1[2] = 'Software'
print(my_dict1)

my_dict1[3] = 'Microsoft Technologies'
print(my_dict1)


# mixing data types in a dictionary
my_dict1[4] = 'Operating Systems'
my_dict1['Bill Gates'] = 'Owner'
print(my_dict1)


# deleting items from dictionaries
del my_dict1['Bill Gates']
print(my_dict1)

my_dict1.clear()
print(my_dict1)
