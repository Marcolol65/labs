def write_input_to_file(filename):
    while True:
        user_input = input("Введите данные для записи в файл (для завершения введите 'exit'): ")
        if user_input.lower() == 'exit':
            break
        with open(filename, 'a') as file:
            file.write(user_input + '\n')

def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [float(line.strip()) for line in file.readlines()]
            return numbers
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    except Exception as e:
        print("Ошибка при чтении файла:", e)
        return []

def calculate_and_append_stats(numbers, filename):
    try:
        total_sum = sum(numbers)
        max_value = max(numbers)
        min_value = min(numbers)

        with open(filename, 'a') as file:
            file.write(f"Сумма: {total_sum}\n")
            file.write(f"Максимум: {max_value}\n")
            file.write(f"Минимум: {min_value}\n")
    except Exception as e:
        print("Ошибка при записи в файл:", e)

filename = 'data.txt'

# Запись ввода пользователя в файл
write_input_to_file(filename)

# Чтение чисел из файла и вычисление статистики
numbers_from_file = read_numbers_from_file(filename)
calculate_and_append_stats(numbers_from_file, filename)