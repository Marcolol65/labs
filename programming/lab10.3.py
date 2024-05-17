import time
import mpmath


# Define the search algorithms
def binary_search(func, a, b, epsilon):
    start_time = time.time()
    while abs(b - a) > epsilon:
        mid = (a + b) / 2
        if func(mid) == 0:
            return mid
        elif func(a) * func(mid) < 0:
            b = mid
        else:
            a = mid
    end_time = time.time()
    return end_time - start_time


def golden_ratio_search(func, a, b, epsilon):
    start_time = time.time()
    phi = (1 + mpmath.sqrt(5)) / 2
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
    end_time = time.time()
    return end_time - start_time


def interpolating_search(func, a, b, epsilon):
    start_time = time.time()
    while abs(b - a) > epsilon:
        x = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if func(x) == 0:
            return x
        elif func(a) * func(x) < 0:
            b = x
        else:
            a = x
    end_time = time.time()
    return end_time - start_time


# Function to find the position of a sequence in π
def find_sequence(sequence, precision=1000000):  # Increased precision to 1,000,000
    with mpmath.workdps(precision):
        pi_digits = str(mpmath.pi)
    sequence_str = str(sequence)
    index = pi_digits.find(sequence_str)
    return index


# Define the sequences
sequences = {
    "six 9": 999999,
    "six 8": 888888,
    "six 0": 000000,
    "the first six digits": int(mpmath.pi * 10**6),
    "seven digits of your phone number": 5522726
}

# Compute and print the execution time of each algorithm for each sequence
for desc, seq in sequences.items():
    print(f"Sequence: {desc}")
    print("Binary Search:", binary_search(lambda x: find_sequence(seq), 0, 1000000, 1e-9))
    print("Golden Ratio Search:", golden_ratio_search(lambda x: find_sequence(seq), 0, 1000000, 1e-9))
    print("Interpolating Search:", interpolating_search(lambda x: find_sequence(seq), 0, 1000000, 1e-9))
    print()