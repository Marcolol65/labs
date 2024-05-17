def sum_of_digits():
    while True:
        user_input = input("Введите целые числа (для завершения введите 'done'): ")
        clean_input = ''.join(filter(str.isdigit, user_input))  # Фильтруем только цифры из ввода

        if clean_input:  # Если строка после фильтрации не пустая
            numbers = list(map(int, clean_input))  # Преобразуем каждую цифру в целое число
            total_sum = sum(numbers)  # Считаем сумму цифр
            print("Сумма введенных цифр:", total_sum)
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите цифры.")


# Вызываем функцию для выполнения программы
sum_of_digits()