def write_data_to_file(data):
    try:
        with open("data.txt", "a") as file:
            file.write(data + "\n")
    except Exception as e:
        print("An error occurred while writing to the file:", e)


def read_and_process_data():
    numbers = []
    try:
        with open("data.txt", "r") as file:
            for line in file:
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    pass
    except FileNotFoundError:
        print("File 'data.txt' not found.")
        return

    if numbers:
        sum_numbers = sum(numbers)
        max_number = max(numbers)
        min_number = min(numbers)

        try:
            with open("data.txt", "a") as file:
                file.write("\nSum: {}\n".format(sum_numbers))
                file.write("Max: {}\n".format(max_number))
                file.write("Min: {}\n".format(min_number))
        except Exception as e:
            print("An error occurred while writing results to the file:", e)
    else:
        print("No valid numbers found in the file.")


while True:
    user_input = input("Enter data (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    else:
        write_data_to_file(user_input)


read_and_process_data()
