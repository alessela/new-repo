from modul_tema2 import *


def suma(*args, **kwargs):
    s = 0
    for k in args:
        try:
            s += k
        except TypeError:
            continue
    for v in kwargs:
        try:
            s += v
        except TypeError:
            continue
    return s


def isInteger():
    print('Citeste o valoare: ')
    x = input()
    try:
        x = int(x)
    except ValueError:
        return 0
    return x


if __name__ == '__main__':
    print(suma(1, 5, -3, 'abc', [12, 56, 'cad']))
    print(suma())
    print(suma(2, 4, 'abc', param_1=2))
    print(isInteger())
    n = 8
    print('Suma numerelor de la 0 la {} este {}'.format(n, sumN(n)))
    print('Suma numerelor impare de la 0 la {} este {}'.format(n, sumOddN(n)))
    print('Suma numerelor pare de la o la {} este {}'.format(n, sumEvenN(n)))
