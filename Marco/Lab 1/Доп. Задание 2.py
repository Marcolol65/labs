print(f'Введите число')
a = int(input())
print(f'Вы ввели {a}')
x = 0
while True:
    while a >= 10:
        x += a % 10
        a = a // 10
    if a > 0:
        x += a
        print(x)
        a = x
        x = 0
    if a < 10:
        break

