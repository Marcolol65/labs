def remove_duplicates_and_spaces(input_string):
    unique_chars = []
    for char in input_string:
        if char != ' ' and char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)


user_input = input("Enter a string: ")
result = remove_duplicates_and_spaces(user_input)
print("Result after removing duplicates and spaces:", result)