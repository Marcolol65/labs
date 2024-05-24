def karatsuba(x, y):
    if len(x) == 1 and len(y) == 1:
        return int(x[0]) * int(y[0])

    n = max(len(x), len(y))

    x = ['0'] * (n - len(x)) + x
    y = ['0'] * (n - len(y)) + y

    mid = n // 2
    a, b = x[:mid], x[mid:]
    c, d = y[:mid], y[mid:]

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(add_lists(a, b), add_lists(c, d)) - ac - bd

    return (10 ** (2 * mid)) * ac + (10 ** mid) * ad_bc + bd


def add_lists(x, y):
    n = max(len(x), len(y))
    x = ['0'] * (n - len(x)) + x
    y = ['0'] * (n - len(y)) + y

    result = []
    carry = 0
    for i in range(n - 1, -1, -1):
        digit_sum = int(x[i]) + int(y[i]) + carry
        carry = digit_sum // 10
        result.insert(0, str(digit_sum % 10))
    if carry:
        result.insert(0, str(carry))

    return result


x = list("123456")
y = list("987654")
result = karatsuba(x, y)
print("Result:", result)
