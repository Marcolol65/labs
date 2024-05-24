def Q_rsqrt(number):
    three_halfs = 1.5

    i = number
    '''
        The value 0x5f3759df is a hexadecimal constant that plays a crucial role in 
        the fast inverse square root algorithm. 
        It's a magic number that helps in the approximation of the inverse square root efficiently.
    '''
    i = 0x5f3759df - (i >> 1)

    y = i
    y = y * (three_halfs - (number * y * y))
    return y


def compute_error(actual, approx):
    return abs(actual - approx) / actual * 100


number = 2.0
actual_result = 1 / number ** 0.5
approx_result = Q_rsqrt(int(number))
error = compute_error(actual_result, approx_result)

print("Actual Result:", actual_result)
print("Approximate Result:", approx_result)
print("Error:", error, "%")
