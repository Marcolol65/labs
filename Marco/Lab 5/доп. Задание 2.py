def find_max_zeros_and_sum(table):
    ind_row, ind_col = 0, 0
    max_num_zeros = -10 ** 20
    max_sum = -10 ** 20
    for ind, row in enumerate(table):
        if row.count(0) > max_num_zeros:
            max_num_zeros, ind_row = row.count(0), ind
    table_rev = [list(i) for i in zip(*table)]
    for ind, col in enumerate(table_rev):
        if sum(col) > max_sum:
            max_sum, ind_col = sum(col), ind
    return f'Максимально нулей в строчке: {ind_row + 1}, Максимальная сумма в столбце: {ind_col + 1}'


def generate_table(n, *args):
    t = [[0] * n for _ in range(n)]
    i, j = 0, 0
    for k in args:
        t[i][j] = k
        if i <= j + 1 and i + j < n - 1:
            j += 1
        elif i < j and i + j >= n - 1:
            i += 1
        elif i >= j and i + j > n - 1:
            j -= 1
        elif i > j + 1 and i + j <= n - 1:
            i -= 1
    return t


table = generate_table(5, 7, 8, 9, 10, 6, 1, 1, 2, 3, 7, 9, 9, 1, 1, 2, 2, 3, 4, 5, 9, 7, 8, 3, 6, 5)
print(*table, sep='\n')
print(find_max_zeros_and_sum(table))
