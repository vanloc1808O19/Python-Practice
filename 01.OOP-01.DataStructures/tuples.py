stock1 = 'MST', 95.00, 97.45, 92.45
stock2 = ('MST', 95.00, 97.45, 92.45)

print(type(stock1))
print(type(stock2))

print(stock1 == stock2)

# define a tuple
tupl = ('Tuple', 'is', 'an', 'IMMUTABLE', 'list')
print(tupl)
print(tupl[0])
print(tupl[-1])
print(tupl[1:3])

# Python tuple methods
# tupl.append('new')  # error
print(tupl.index('IMMUTABLE'))
# print(tupl.index('new')) # error
print(tupl.count('list'))