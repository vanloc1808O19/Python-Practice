# functions are objects too
def my_func():
    print('My function was called')


my_func.description = 'A silly function'


def second_func():
    print('Second function was called')


second_func.description = 'One more sillier function'


def another_func(func):
    print("The description:", end=" ")
    print(func.description)
    print('The name:', end=" ")
    print(func.__name__)
    print('The class:', end=' ')
    print(func.__class__)
    print("Now I'll call the function passed in")
    func()


another_func(my_func)
another_func(second_func)
