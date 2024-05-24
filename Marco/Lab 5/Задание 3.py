a = input('Пиши циферки,чиселки и если скучно буковки, устанешь - жми Enter: ')
summ = 0

while a != '':
    if a.isdigit():
        summ += int(a)
        print('Cумма чисел =', summ)
        a = input('Следующее число: ')
    else:
        for i in range(len(a)):
            b = ''
            if a[i].isdigit():
                b += a[i]
                summ += int(b)
        print('Сумма чисел =', summ)
        a = input('Следующее число: ')

print('Сумма чисел =', summ)

