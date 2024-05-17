import math

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def calculate_x_n(n):
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    x_n = 0.5 * (phi**(n+1) - psi**(n+1))
    return x_n

def find_n_with_error_threshold(error_threshold):
    n = 1
    while True:
        F_n = fibonacci(n)  # Вычисляем n-е число Фибоначчи
        x_n = calculate_x_n(n)  # Вычисляем x_n по формуле
        error = abs(x_n - F_n)
        if error > error_threshold:
            return n
        n += 1

# Находим n, начиная с которого ошибка превысит 0.001
threshold = 0.001
result_n = find_n_with_error_threshold(threshold)
print(f"Начиная o n = {result_n}, разница превышает {threshold}.")