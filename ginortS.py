import string
from collections import OrderedDict
from timeit import timeit


def f1(input_string):
    return sorted(input_string, key=lambda c: (-ord(c) >> 5, c in '02468', c))


def f2(input_string):
    return sorted(input_string, key=lambda c: (c.isdigit() - c.islower(), c in '02468', c))


def f3(input_string):
    order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
    return sorted(input_string, key=order.index)


# COOL
def f4(input_string):
    return sorted(input_string, key=(string.ascii_letters + '1357902468').index)


def my_fast_func(input_string):
    order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
    return sorted(input_string, key=dict(zip(order, range(len(order)))).get)


def my_func(input_string):
    char_categories = OrderedDict({'lowers': '', 'uppers': '', 'odds': '', 'evens': ''})
    pairs = list(zip(char_categories.keys(), (string.ascii_lowercase, string.ascii_uppercase, '13579', '02468')))

    for char in input_string:
        for key, set_ in pairs:
            if char in set_:
                char_categories[key] += char

    for k, v in char_categories.items():
        char_categories[k] = ''.join(sorted(char_categories[k]))

    return char_categories.values()


# def my_func2(input_string):
#     d = dict(zip())

if __name__ == '__main__':
    test_str = 'I86E24gV3dfNQ2NVI2P2T5UdVyqPw8jN0EACrH31X3174LIdr5jd21ML5w2t3229QdQq85PAhUX5LU33h6347qe21458Nd7j7L5802wJe126w0rEL89VIw94M7G56fy39HJ11XMF3A515fI745E5fEjy9D91SI1LA83M4M578S40j35K7rJhM1fHUDTQW36WKwS2fMq5G4GA8q3SF4RgE213Wf9BK1C49yRwB87jMQOWV3615HUMq6Y7D9yHtT1It422J574IhDw6yT1GSGTTH53fN1OHY5GeD94941JOC4FV1NEj7Dq496Z463h1F5FVJ3RQ5P45N4452rGK8U3J18M1LGMMj4LLYVw17BIfZUhZMgV482Ij462O19Vt813N57N4wNS8hTqF3WHO4Dq79yLJLP9WjwTwC75e66DX34697W1tM19K8VP3qqgVJ4MRdHX4BMfO666dP9B3BS14LwDhZ65LhHwQeTY98MMjqJ5etq7X2YWrhYeVMyj15HI754W7XKZhJ93W2qXJ1C83M2Fe6445HeR1873r262fHM88XQ3L558Q8yH574Rw88rAw4U0rJJ8j2Q932M59ROqVwG3D3jXfIMX639EfINGJ6BgS3r6tWH7ZUV841127dK6JAeES61T72LeeW7r31Aw76eAy73wU6R43Z65jf0hW8rR81hPJFe5T27VLrM6DgTyBJU4yrS6qRht6P7y99Xw93R12Lq7e4UPM1A9ZEWSI8rAfH3Z5S5A3SeYDyJ1140h4dJUOO9F1IQ8M705e6YH5WJ31H5OHyY442rB9392FL7DR35FO14f2K42A18J0d14FEWj83TA0568w16dd52843NO867gT64VH5VU429r648CB9B9rSF9QCPf276dXGO5rOB3499d6841OB0852Af8455y3HH52rj3R57183822d8tO321e124V47N1J3OHNV3SQ3j1DyLt5HhC7F67CZd3DWyEgN7'
    print(f'mf: {timeit(lambda: my_fast_func(test_str), number=10_000)} s')
    print(f'f3: {timeit(lambda: f3(test_str), number=10_000)} s')
    print(f'f4: {timeit(lambda: f4(test_str), number=10_000)} s')
    print(f'f1: {timeit(lambda: f1(test_str), number=10_000)} s')
    print(f'f2: {timeit(lambda: f2(test_str), number=10_000)} s')
    print(f'my: {timeit(lambda: my_func(test_str), number=10_000)} s')
