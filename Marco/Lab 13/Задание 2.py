from Задание_1 import *
def concurrentScalarProduct(vs):
    sum = 0
    with ThreadPoolExecutor() as executor:
        results = [executor.submit(lambda fx: fx[0] * fx[1], [vs[0][i], vs[1][i]]) for i in range(len(vs[0]))]
        for future in as_completed(results):
            sum += future.result()
    return sum


def getMatrix():
    return np.array(eval(input('Введите матрицу в одну строку, используя квадратные скобочки и запятые: ')))


def getVectors(matrix, axis=0):
    vectors = []
    if axis != 0:
        matrix = matrix.transpose()
    if len(list(matrix.shape)) <= 1:
        vectors = [list(matrix)]
    else:
        for line in matrix:
            vectors.append(list(line))
    return vectors


def concurrentMatrixProduct(vs1, vs2):
    with ThreadPoolExecutor() as executor:
        holder = [0] * len(vs1) * len(vs2)
        index = 0
        for v1 in vs1:
            for v2 in vs2:
                holder[index] = [v1, v2]
                index += 1
        results = list(executor.map(concurrentScalarProduct, holder))
        results = np.array([results]).reshape(len(vs1), len(vs2))
        return results


vectors1 = getVectors(getMatrix())
vectors2 = getVectors(getMatrix(), axis=1)
print()
print(concurrentMatrixProduct(vectors1, vectors2))
