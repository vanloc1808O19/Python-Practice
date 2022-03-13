# len() function
print(len(['hello', 9, 45.0, 24, True]))

set1 = {1, 2, 3, 4}
print(set1.__len__())

# reversed(seq)
normal_list = [2, 4, 5, 7, 9]


class CustomSequence:
    def __len__(self):
        return 5

    def __getitem__(self, index):
        return "x{0}".format(index)


class FunkyBack:
    def __reversed__(self):
        return 'backwards!'


for seq in normal_list, CustomSequence(), FunkyBack():
    print('\n{}: '.format(seq.__class__.__name__), end="")
    for item in reversed(seq):
        print(item, end=", ")
print("")

# enumerate
names = ['Lionel', 'Andres', 'Messi', 'Nguyen', 'Van', 'Loc']
print(enumerate(names))

print(list(enumerate(names)))

for i, n in enumerate(names):
    print('Names number: ' + str(i))
    print(n)
