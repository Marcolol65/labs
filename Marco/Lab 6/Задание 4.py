def read_matrix(filename):
    try:
        with open(filename, 'r') as file:
            matrix = [list(map(int, line.strip().split())) for line in file]
        return matrix
    except FileNotFoundError:
        print("File '{}' not found.".format(filename))
        return None


def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Cannot multiply matrices: incompatible dimensions.")
        return None

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
            row.append(element)
        result.append(row)
    return result


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


def main():
    matrix1_filename = input("Enter the filename of the first matrix: ")
    matrix2_filename = input("Enter the filename of the second matrix: ")

    matrix1 = read_matrix(matrix1_filename)
    matrix2 = read_matrix(matrix2_filename)
    '''
    matrix1 = read_matrix(matrixfile1.txt)
    matrix2 = read_matrix(matrixfile2.txt)
    '''

    if matrix1 and matrix2:
        result = multiply_matrices(matrix1, matrix2)
        if result:
            print("Result:")
            print_matrix(result)


if __name__ == "__main__":
    main()
