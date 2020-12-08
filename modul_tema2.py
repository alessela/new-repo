def sumN(n):
    if n == 0:
        return 0
    return n + sumN(n - 1)


def sumEvenN(n):
    if n < 2:
        return 0
    if n % 2 == 1:
        return sumEvenN(n - 1)
    return n + sumEvenN(n - 2)


def sumOddN(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        return sumOddN(n - 1)
    return n + sumOddN(n - 2)
