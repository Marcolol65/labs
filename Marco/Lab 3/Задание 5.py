def get_input():
    return input("Enter a value: ")


def test_input(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def str_to_int(value):
    return int(value)


def print_int(value):
    print(value)


input_value = get_input()

if test_input(input_value):
    int_value = str_to_int(input_value)
    print_int(int_value)
else:
    print("Input cannot be converted to an integer.")
