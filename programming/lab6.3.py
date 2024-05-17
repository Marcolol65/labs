def read_occupation_from_file(filename):
    try:
        with open(filename, 'r') as file:
            rows = [line.strip() for line in file.readlines()]
            return rows
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    except Exception as e:
        print("Ошибка при чтении файла:", e)
        return []

# Пример использования
filename = "occupation.txt"
occupation_data = read_occupation_from_file(filename)
if occupation_data:
    for i, row in enumerate(occupation_data, start=1):
        print(f"Ряд {i}: {row}")