def read_seat_info(filename):
    try:
        with open(filename, 'r') as file:
            seats = [list(map(int, line.strip().split())) for line in file]
        return seats
    except FileNotFoundError:
        print("File '{}' not found.".format(filename))
        return None


def count_free_seats(seats):
    total_seats = sum(len(row) for row in seats)
    free_seats = sum(row.count(0) for row in seats)
    return total_seats, free_seats


def count_free_seats_in_row(seats, row_number):
    if 1 <= row_number <= len(seats):
        free_seats = seats[row_number - 1].count(0)
        return free_seats
    else:
        print("Invalid row number.")
        return None


def is_seat_free(seats, row_number, seat_number):
    if 1 <= row_number <= len(seats) and 1 <= seat_number <= len(seats[row_number - 1]):
        return seats[row_number - 1][seat_number - 1] == 0
    else:
        print("Invalid row or seat number.")
        return None


def main():
    filename = input("Enter the filename: ")
    seats = read_seat_info(filename)
    if seats:
        total_seats, free_seats = count_free_seats(seats)
        print("Total seats:", total_seats)
        print("Free seats:", free_seats)

        for i, row in enumerate(seats, 1):
            free_seats_in_row = row.count(0)
            print("Row {}: {} free seats".format(i, free_seats_in_row))

        row_number = int(input("Enter the row number: "))
        seat_number = int(input("Enter the seat number: "))
        if is_seat_free(seats, row_number, seat_number):
            print("Seat {} in row {} is free.".format(seat_number, row_number))
        else:
            print("Seat {} in row {} is occupied.".format(seat_number, row_number))


if __name__ == "__main__":
    main()
