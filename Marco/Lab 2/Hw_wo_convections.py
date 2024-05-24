A = int(input("Enter the first integer: "))
B = int(input("Enter the second integer: "))

result = A - B
result_sign = (result >> 31) & 1
max_value = A - result_sign * result

print("The maximum value is:", max_value)