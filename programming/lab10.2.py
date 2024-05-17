import math


def binary_search(func, a, b, epsilon):
    while abs(b - a) > epsilon:
        mid = (a + b) / 2
        if func(mid) == 0:
            return mid
        elif func(a) * func(mid) < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2


def golden_ratio_search(func, a, b, epsilon):
    phi = (1 + math.sqrt(5)) / 2
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    f1 = func(x1)
    f2 = func(x2)
    while abs(b - a) > epsilon:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - (b - a) / phi
            f1 = func(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (b - a) / phi
            f2 = func(x2)
    return (a + b) / 2


def interpolating_search(func, a, b, epsilon):
    while abs(b - a) > epsilon:
        x = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if func(x) == 0:
            return x
        elif func(a) * func(x) < 0:
            b = x
        else:
            a = x
    return (a + b) / 2
