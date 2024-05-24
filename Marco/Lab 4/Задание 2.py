def divide_pie(n):
    pieces_guests_1 = n
    pieces_needed_2 = 2 * (n // 2) - (n % 2)
    pieces_guests_1_plus_10 = n + 10
    return pieces_guests_1, pieces_needed_2, pieces_guests_1_plus_10


def main():
    a = int(input("Enter the number of guests: "))
    pieces_1, pieces_2, pieces_1_plus_10 = divide_pie(a)

    print("To ensure:")
    print("- Each guest gets at least 1 piece, you need", pieces_1, "pieces.")
    print("- At least half of the guests get 2 pieces each, you need", pieces_2, "pieces.")
    print("- Each guest gets 1 piece and at least 10 more pieces are left in stock, you need",
          pieces_1_plus_10, "pieces.")


if __name__ == "__main__":
    main()
