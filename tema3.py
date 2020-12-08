from math import floor


def gcd(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


class Fractie:
    def __init__(self, numa, numi):
        d = gcd(numa, numi)
        self.numa = numa / d
        self.numi = numi / d

    def __str__(self):
        return f'{floor(self.numa)}/{floor(self.numi)}'

    def __add__(self, other):
        numa = self.numa * other.numi + self.numi * other.numa
        numi = self.numi * other.numi
        return Fractie(numa, numi)

    def __sub__(self, other):
        numa = self.numa * other.numi - self.numi * other.numa
        numi = self.numi * other.numi
        return Fractie(numa, numi)

    def inverse(self):
        if self.numa == 0:
            return None  # 0 nu are inversa
        return Fractie(self.numi, self.numa)


a = Fractie(36, 60)
b = Fractie(20, 15)
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(b, a, b - a))
print('1 / ({}) = {}'.format(a, a.inverse()))
