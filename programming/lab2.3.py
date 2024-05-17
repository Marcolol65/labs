N = int(input("Enter the upper bound of the range (N): "))

low = 1
high = N

while low <= high:
    mid = (low + high) // 2
    answer = input(f"Is your number greater than, less than, or equal to {mid}? (Enter 'greater', 'less', or 'equal'): ")
    if answer == "greater":
        low = mid + 1
    elif answer == "less":
        high = mid - 1
    else:
        print(f"The number you guessed is: {mid}")
        break