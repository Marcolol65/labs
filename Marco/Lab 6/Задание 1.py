def write_numbers_to_file(numbers):
    try:
        with open("numbers.txt", "w") as file:
            for number in numbers:
                file.write(str(number) + "\n")
    except Exception as e:
        print("An error occurred while writing to the file:", e)


def read_numbers_from_file():
    numbers = []
    try:
        with open("numbers.txt", "r") as file:
            for line in file:
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    pass
    except FileNotFoundError:
        print("File 'numbers.txt' not found.")
        return

    if numbers:
        sum_numbers = sum(numbers)
        max_number = max(numbers)
        min_number = min(numbers)

        try:
            with open("numbers.txt", "a") as file:
                file.write("\nSum: {}\n".format(sum_numbers))
                file.write("Max: {}\n".format(max_number))
                file.write("Min: {}\n".format(min_number))
        except Exception as e:
            print("An error occurred while writing results to the file:", e)
    else:
        print("No numbers found in the file.")


input_numbers = input("Enter numbers separated by spaces: ").split()


numbers = []
for input_number in input_numbers:
    try:
        number = float(input_number)
        numbers.append(number)
    except ValueError:
        print(f"Warning: '{input_number}' is not a valid number.")


write_numbers_to_file(numbers)
read_numbers_from_file()
