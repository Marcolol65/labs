x = int(input("Enter a number: "))

is_three_digit_with_zero_end = 100 <= x <= 999 and x % 10 == 0
is_odd_and_divisible_by_3_or_5 = x % 2 != 0 and (x % 3 == 0 or x % 5 == 0)
is_in_interval_2_to_6 = 2 <= x <= 6
is_three_digit_with_same_digits = 100 <= x <= 999 and str(x)[0] == str(x)[1] == str(x)[2]

result = is_three_digit_with_zero_end or \
         is_odd_and_divisible_by_3_or_5 or \
         is_in_interval_2_to_6 or \
         is_three_digit_with_same_digits

print("Result of the logical expression:", result)