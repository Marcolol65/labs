from concurrent.futures import ThreadPoolExecutor, as_completed
import numpy as np

v1 = np.array(list(map(float, input('Введите координаты первого вектора через пробел: ').split())))
v2 = np.array(list(map(float, input('Введите координаты второго вектора через пробел: ').split())))

sum = 0
with ThreadPoolExecutor(max_workers=4) as executor:
    results = [executor.submit(lambda fx: fx[0] * fx[1], [v1[i], v2[i]]) for i in range(len(v1))]
    for future in as_completed(results):
        sum += future.result()

print(f'Результат равен {sum}')
