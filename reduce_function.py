from fractions import Fraction
from functools import reduce


def product(fracs):
    t = reduce(lambda f1, f2: f1 * f2, fracs)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        # fracs.append(Fraction(*map(int, input().split())))
        fracs.append(Fraction(*(int(x) for x in input().split())))
    result = product(fracs)
    print(*result)
