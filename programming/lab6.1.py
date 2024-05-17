def write_numbers_to_file(numbers, filename):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [float(line.strip()) for line in file.readlines()]
            return numbers
    except FileNotFoundError:
        print("Файл не найден.")
        return None
    except Exception as e:
        print("Ошибка при чтении файла:", e)
        return None

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

# Ввод чисел с клавиатуры
numbers_input = input("Введите числа через пробел: ").split()
numbers = [float(number) for number in numbers_input]

# Запись чисел в файл
write_numbers_to_file(numbers, 'numbers.txt')

# Чтение чисел из файла и вычисление статистики
numbers_from_file = read_numbers_from_file('numbers.txt')
if numbers_from_file:
    calculate_and_append_stats(numbers_from_file, 'numbers.txt')