def reverse_dictionary(dict_items):
    reversed_dict = {}  # Создаем пустой словарь для обратных значений
    for number, string in dict_items:
        reversed_dict[string] = number  # Заполняем обратный словарь значениями из исходного
    return reversed_dict

# Создаем исходный словарь
original_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four"
}

# Получаем представление словаря в виде dict_items
dict_items = original_dict.items()

# Вызываем функцию reverse_dictionary и передаем ей dict_items
reversed_dict = reverse_dictionary(dict_items)

# Выводим обратный словарь
print("Обратный словарь:")
print(reversed_dict)