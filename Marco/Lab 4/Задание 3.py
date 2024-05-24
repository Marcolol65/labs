import math


def find_n_for_accuracy(accuracy):
    def fib_formula(n):
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        return (phi ** (n + 1) - psi ** (n + 1)) / sqrt5

    def fib(n):
        if n <= 1:
            return n
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    n = 0
    while True:
        fib_n_formula = fib_formula(n)
        fib_n_actual = fib(n)
        if abs(fib_n_formula - fib_n_actual) > accuracy:
            break
        n += 1

    return n


accuracy = 0.001
result_n = find_n_for_accuracy(accuracy)
print("The smallest value of n where the difference exceeds", accuracy, "is:", result_n)
