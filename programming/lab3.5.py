def getInput():
    return input("Enter a value: ")

def testInput(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def strToInt(value):
    return int(value)

def printInt(value):
    print(value)


input_value = getInput()

if testInput(input_value):
    int_value = strToInt(input_value)
    printInt(int_value)
else:
    print("Input cannot be converted to an integer.")