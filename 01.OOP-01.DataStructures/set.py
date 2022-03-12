"""
    Though sets in general can be implemented using trees,
    set in Python can be implemented using a hash table.
"""

# create a set

# set of integers
my_set = {1, 2, 4, 8}
print(my_set)

# set of mixed data types
my_set1 = {1.0, "Hello World!", (2, 4, 6)}
print(my_set1)


# methods for sets

# add(x) method
topics = {'Python', 'Java', 'C++'}
topics.add('SQL')
print(topics)

team = {'Developer', 'Content Writer', 'Editor', 'Tester'}

group = topics.union(team)
print(group)

inters = topics.intersection(team)
print(inters)

# difference(s) method, returns a set containing all the elements of
# invoking set but not of the second set

safe = topics.difference(team)
print(safe)

diff = topics.difference(group)
print(diff)

group.clear()
print(group)


# Python set operators

# create two sets
set1 = set()
set2 = set()

# add elements to set
for i in range(1, 5):
    set1.add(i)

for j in range(4, 9):
    set2.add(j)

print(set1)
print(set2)

# union of set1 and set 2
set3 = set1 | set2  # same as set1.union(set2)
print(set3)

# intersection of set1 and set2
set4 = set1 & set2  # same as set1.intersection(set2)
print(set4)

# check relation between set3 and set4
if set3 > set4:  # set3.issuperset(set4)
    print('Set3 is superset of set4')
elif set3 < set4:  # set3.issubset(set4)
    print('Set3 is subset of set4')
else:  # set3 == set4
    print('Set3 is the same as set4')

# difference between set3 and set4
set5 = set3 - set4
print(set5)

# check if set4 and set5 are disjoint sets
if set4.isdisjoint(set5):
    print('Set4 and set5 have nothing in common')
else:
    print('Set4 and set5 have something in common')

# remove all the value of set5
set5.clear()
print(set5)
