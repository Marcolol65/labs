print('Введите первые два числа')
a = float(input())
x = float(input())
if a >= x:
    max_ = a
    min_ = x
else:
    max_ = x
    min_ = a
while a:
    print('Введите числа, чтобы мы узнали какое из них больше, а какое меньше.')
    if a > max_:
        max_ = a
    if a < min_:
        min_ = a
    print(f'На данный момент max:{max_}, min{min_}')
    a = float(input())

