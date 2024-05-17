import mpmath


# Function to find the position of a sequence in π
def find_sequence(sequence, precision=1000000):
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

# Compute and print the positions of the sequences
for desc, seq in sequences.items():
    position = find_sequence(seq)
    print(f"The position of {desc} in π is:", position)