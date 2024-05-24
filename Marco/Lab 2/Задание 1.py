def is_symmetric_number(number):
    number_str = str(number).zfill(4)
    return number_str == number_str[::-1]


if __name__ == "__main__":
    try:
        number = int(input("Enter a four-digit number: "))
        if is_symmetric_number(number):
            print(1)
        else:
            print(0)
    except ValueError:
        print("Enter valid data")
