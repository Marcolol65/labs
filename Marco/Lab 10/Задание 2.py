def binary(listic, key):
    short = 0
    high = len(listic)
    while short < high:
        mid = (short + high) // 2
        if key == listic[mid]:
            return mid
        elif key < listic[mid]:
            high = mid
        else:
            short = mid
    return 'Нет('


def gold(listic, key):
    phi = 0.5*(1 + 5 ** 0.5)
    x = 0
    y = len(listic) - 1
    while y - x >= 1:
        x1 = int(y - (y - x)//phi)
        x2 = int(x + (y - x)//phi)
        X = listic[x : x2 + 1]
        Y = listic[x1 : y + 1]
        if key in X:
            y = x2
        elif key in Y:
            x = x1
        else:
            print('Нет(')
    return x


def interpolation(listic, key):
    short = 0
    high = len(listic) - 1

    while short <= high:
        i = short + ((high - short) * (key - listic[short]) // (listic[high] - listic[short]))

        if key == listic[i]:
            return i
        elif key < listic[i]:
            high = i - 1
        else:
            short = i + 1


oblast = [0, 5, 7, 9, 11, 13, 16, 17, 19, 20, 33, 45, 68]

print(binary(oblast, 17))
print(gold(oblast, 17))
print(interpolation(oblast, 17))