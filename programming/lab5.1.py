def transform_string(s):
    # Подсчитываем количество символов в верхнем и нижнем регистрах
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())

    # Принимаем решение о регистре для вывода
    if upper_count > lower_count:
        # Если больше символов в верхнем регистре, преобразуем всю строку к верхнему регистру
        return s.upper()
    elif lower_count > upper_count:
        # Если больше символов в нижнем регистре, преобразуем всю строку к нижнему регистру
        return s.lower()
    else:
        # Если количество символов в верхнем и нижнем регистрах одинаково, возвращаем оригинальную строку
        return s


# Ввод строки с клавиатуры
input_string = input("Введите строку: ")

# Вызываем функцию для преобразования строки и выводим результат
transformed_string = transform_string(input_string)
print("Преобразованная строка:", transformed_string)