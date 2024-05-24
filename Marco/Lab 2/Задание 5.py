def process_sequence():
    numbers = []
    count = 0
    while True:
        number = int(input("Enter a non-negative integer (0 to stop): "))
        if number < 0:
            raise ValueError("We dont take negativity here, sir! Seriously use a positive integer")
        if number == 0:
            break
        numbers.append(number)
        count += 1

    print(15*"=", "Ops", 15*"=")
    print("1. Sum |\n2. Product |\n3. Average |\n4. Max number |\n 5. Min number |\n 6. Count odd and even |")
    print(15 * "=", "Ops", 15 * "=")
    20
    operation = input("Choose operation (1-6): ")
    if operation == '1':
        print("Sum of entered numbers:", sum(numbers))
    elif operation == '2':
        result = 1
        for num in numbers:
            result *= num
        print("Product of entered numbers:", result)
    elif operation == '3':
        print("Average of entered numbers:", sum(numbers) / count)
    elif operation == '4':
        print("Maximum of entered numbers:", max(numbers))
    elif operation == '5':
        print("Minimum of entered numbers:", min(numbers))
    elif operation == '6':
        even_count = sum(1 for num in numbers if num % 2 == 0)
        odd_count = count - even_count
        print("Number of even elements:", even_count)
        print("Number of odd elements:", odd_count)


if __name__ == "__main__":
    process_sequence()
