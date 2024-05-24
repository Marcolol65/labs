def input_value():
    try:
        value = float(input("Enter a value: "))
        return value
    except ValueError:
        return input("Enter a string: ")


def main():
    print("The program will either sum numbers or concatenate strings.")
    value1 = input_value()
    value2 = input_value()

    if isinstance(value1, str) or isinstance(value2, str):
        result_concat = str(value1) + str(value2)
        print("Concatenation result: ", result_concat)
    else:
        result_sum = value1 + value2
        print("Sum result: ", result_sum)


if __name__ == "__main__":
    main()
