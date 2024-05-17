def input_value(prompt):
    while True:
        try:
            value = input(prompt)
            float_value = float(value)  # Преобразуем введенное значение в число
            return float_value
        except ValueError:
            # Если не удалось преобразовать в число, возвращаем введенную строку
            return value


def main():
    print("Введите два значения:")

    # Запрашиваем первое значение
    value1 = input_value("Значение 1: ")

    # Запрашиваем второе значение
    value2 = input_value("Значение 2: ")

    # Проверяем типы введенных значений
    if isinstance(value1, str) or isinstance(value2, str):
        # Если хотя бы одно из значений строка, то выполняем конкатенацию
        result = str(value1) + str(value2)
        print("Результат конкатенации:", result)
    else:
        # Иначе складываем числа
        result = value1 + value2
        print("Результат сложения:", result)


if __name__ == "__main__":
    main()