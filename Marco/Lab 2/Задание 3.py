def plural_form(n):
    if n % 10 == 1 and n % 100 != 11:
        return "корова"
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        return "коровы"
    else:
        return "коров"


if __name__ == "__main__":
    n = int(input("Enter the number of cows: "))
    print(f"На лугу пасется {n} {plural_form(n)}")
