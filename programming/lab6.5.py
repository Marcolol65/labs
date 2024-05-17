import os

def find_file_by_name(filename):
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, filename)
    if os.path.exists(file_path):
        return os.path.abspath(file_path)
    else:
        return None

# Имя файла для поиска
filename_to_find = "occupation.txt"

# Поиск файла
file_path = find_file_by_name(filename_to_find)

# Вывод результата
if file_path:
    print(f"Файл '{filename_to_find}' найден по следующему пути:")
    print(file_path)
else:
    print(f"Файл '{filename_to_find}' не найден.")
