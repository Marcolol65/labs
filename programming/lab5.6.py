def reverse_dictionary_letters_to_numbers(input_dict):
    reversed_dict = {}  # Создаем пустой словарь для обратных значений
    for key, value in input_dict.items():
        for char in value:
            if char.isalpha():  # Проверяем, является ли символ буквой
                if char in reversed_dict:
                    reversed_dict[char] = int(str(reversed_dict[char]) + str(key))  # Добавляем цифру к числу
                else:
                    reversed_dict[char] = key  # Создаем новую запись в обратном словаре
    return reversed_dict

# Создаем исходный словарь
original_dict = {
    1: 'аcc',
    2: 'сab',
    3: 'ccb'
}

# Вызываем функцию reverse_dictionary_letters_to_numbers и передаем ей исходный словарь
reversed_dict = reverse_dictionary_letters_to_numbers(original_dict)

# Выводим обратный словарь
print("Обратный словарь:")
print(reversed_dict)