def min_fry(k, m, n):
    fry_times = n // k

    if n % k != 0:
        fry_times += 1

    time = fry_times * (2 * m)
    return time


def main():
    k = int(input("Enter the number of cutlets, that can be fried simultaneously: "))
    m = int(input("Enter the frying time per side in minutes: "))
    n = int(input("Enter how many cutlets are to be fried: "))

    print(f"The minimum required time to fry {n} cutlets on both sides is {min_fry(k,m,n)} minutes")


if __name__ == "__main__":
    main()
