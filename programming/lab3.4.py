def test():
    num = int(input("Enter an integer: "))
    if num > 0:
        positive()
    elif num < 0:
        negative()

def positive():
    print("Positive")

def negative():
    print("Negative")

test()
