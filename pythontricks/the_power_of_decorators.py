# 3.3 The power of decorators

def the_most_basic():
    def null_decorator(func):
        return func

    def greet():
        return 'Hi'

    greet = null_decorator(greet)
    print(greet())


def using_decorator_syntax():
    def null_decorator(func):
        return func

    @null_decorator
    def greet():
        return 'Hi'

    print(greet())


def a_useful_decorator():
    from string import ascii_letters
    from random import choices

    def uppercase(func):
        return func().upper

    @uppercase
    def random_letters(length: int = 10):
        return ''.join(choices(ascii_letters, k=length))

    print(random_letters())


if __name__ == '__main__':
    the_most_basic()
    using_decorator_syntax()
    a_useful_decorator()
