def karatsuba_multiply(x, y):
    # Преобразуем x и y из списков [x1, y1] в числа N1 и N2
    N1 = x[0] * T + x[1]
    N2 = y[0] * T + y[1]

    # Если x или y являются однозначными числами, возвращаем их произведение
    if len(str(x[0])) == 1 and len(str(y[0])) == 1:
        return [x[0] * y[0], x[1] * y[1]]

    # Разбиваем числа x и y на более мелкие части
    m = max(len(str(x[0])), len(str(y[0]))) // 2
    x_h = x[0] // 10**m
    x_l = x[0] % (10**m)
    y_h = y[0] // 10**m
    y_l = y[0] % (10**m)

    # Рекурсивно вычисляем необходимые произведения
    z0 = karatsuba_multiply([x_l, x[1]], [y_l, y[1]])
    z1 = karatsuba_multiply([x_h + x_l, x[1]], [y_h + y_l, y[1]])
    z2 = karatsuba_multiply([x_h, x[1]], [y_h, y[1]])

    # Вычисляем результат по формуле Карацубы
    result = [z2[0] * (10**(2*m)) + (z1[0] - z2[0] - z0[0]) * (10**m) + z0[0],
              z0[1] * (10**m) + (z1[1] - x_h*y_h) * (10**m) + z2[1]]

    return result