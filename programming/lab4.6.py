def convert_base(number, from_base, to_base):
    if isinstance(number, str):
        n = int(number, from_base)
    else:
        n = int(number)

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, from_base, to_base) + alphabet[n % to_base]

def add(a, b, base):
    result = int(convert_base(a, base, 10)) + int(convert_base(b, base, 10))
    return convert_base(result, 10, base)

def subtract(a, b, base):
    result = int(convert_base(a, base, 10)) - int(convert_base(b, base, 10))
    return convert_base(result, 10, base)

def multiply(a, b, base):
    result = int(convert_base(a, base, 10)) * int(convert_base(b, base, 10))
    return convert_base(result, 10, base)

def divide(a, b, base):
    result = int(convert_base(a, base, 10)) // int(convert_base(b, base, 10))
    return convert_base(result, 10, base)

# Example
a = "1010"
b = "11"
base = 2

print("A + B =", add(a, b, base))
print("A - B =", subtract(a, b, base))
print("A * B =", multiply(a, b, base))
print("A / B =", divide(a, b, base))