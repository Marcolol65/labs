def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == "__main__":
    try:
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print(f"YES", end=", ")
        else:
            print(f"NO", end=", ")
        print("to leap year!")
    except ValueError:
        print("Insert an actual number")
