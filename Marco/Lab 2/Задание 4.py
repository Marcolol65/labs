# import time


def find_min_divider_for(number):
    for i in range(2, number + 1):
        if number % i == 0:
            return i


def find_min_divider_while(number):
    i = 2
    while i <= number:
        if number % i == 0:
            return i
        i += 1


'''def count_time(func):
    start_time = time.time()
    func
    end_time = time.time()
    return end_time - start_time'''


if __name__ == "__main__":
    number = int(input("Enter an integer (>= 2): "))
    print("Using for loop:", find_min_divider_for(number))
    print("Using while loop:", find_min_divider_while(number))

    '''print(f"Time for for loop: {count_time(find_min_divider_for(number)): .100f}")
    print(f"Time for while loop: {count_time(find_min_divider_while(number)): .100f}")'''
