def read_matrix_from_file(filename):
    try:
        with open(filename, 'r') as file:
            rows = []
            for line in file:
                row = list(map(int, line.strip().split()))
                rows.append(row)
            return rows
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    except Exception as e:
        print("Ошибка при чтении файла:", e)
        return []

def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix1[0])):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    return result

# Чтение матриц из файлов
matrix1 = read_matrix_from_file("matrix1.txt")
matrix2 = read_matrix_from_file("matrix2.txt")

# Умножение матриц
if matrix1 and matrix2:
    product_matrix = multiply_matrices(matrix1, matrix2)
    print("Произведение матриц:")
    for row in product_matrix:
        print(row)