def guess_number(N):
    low = 1
    high = N

    while low <= high:
        mid = (low + high) // 2
        print(f"Is your number {mid}? (yes/no)")
        response = input().lower()

        if response == 'yes':
            print(f"Congratulations! Your number is {mid}.")
            return mid
        elif response == 'no':
            print(f"Is your number less than {mid}? (yes/no)")
            response = input().lower()

            if response == 'yes':
                high = mid - 1
            elif response == 'no':
                low = mid + 1
            else:
                print("Please enter a valid response (yes/no).")
        else:
            print("Please enter a valid response (yes/no).")

    return -1


def main():
    print("Welcome to the number guessing game!")
    print("Please think of a number from 1 to N and I will try to guess it.")

    N = int(input("Enter the maximum value (N): "))

    guessed_number = guess_number(N)

    if guessed_number == -1:
        print("Sorry, I could not guess your number.")
    else:
        print("Game over.")


if __name__ == "__main__":
    main()
