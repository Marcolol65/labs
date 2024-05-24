
from math import sin, acos, cos
import pylab

pi = 3.14159
g = 9.80665

def x_t(v0, a, t):
    return v0 * cos(a) * t

def y_t(v0, a, t):
    return (v0 * sin(a) * t) - (0.5 * g * (t ** 2))


v0 = input('Введите начальную скорость (по умолчанию - 5 м/с):')
if v0 == '':
    v0 = 5
v0 = float(v0)

alpha = input('Введите угол прыжка (по умолчанию - 40 градусов к горизонту):')
if alpha == '':
    alpha = 40
alpha = float(alpha)

alpha = alpha * pi / 180

h_max = (v0 * (sin(alpha) ** 2)) / (2 * g)
l_max = ((v0 ** 2) * sin(alpha * 2)) / g

print('Максимальная высота прыжка равна {} м, а максимальная длина - {} м'.format(h_max, l_max))

cornersForLength = []
for a in range(91):
    cornersForLength.append(v0 ** 2 * sin(2 * a * pi / 180) / g)
print('Начальный угол для максимальной дальности прыжка равен: {}°'
      .format(cornersForLength.index(max(cornersForLength))))


cornersForHeight = []
for a in range(91):
    cornersForHeight.append(v0 ** 2 * sin(a * pi / 180) / g)
print('Начальный угол для максимальной дальности прыжка равен: {}°'
      .format(cornersForHeight.index(max(cornersForHeight))))


x = input('Введите x (по умолчанию - 2 м):')
if x == '':
    x = 2
x = float(x)

y = input('Введите y (по умолчанию - 3 м):')
if y == '':
    y = 3
y = float(y)

t = input('Введите t (по умолчанию - 1 c):')
if t == '':
    t = 1
t = float(t)

v0 = ((y + 0.5 * g * (t ** 2)) ** 2 + x ** 2 / (t ** 2)) ** 0.5
print('Скорость равна {:.5f} м/с.'.format(v0))

alpha = acos(x / (v0 * t))
print('Угол равен {:.5f} радиан, что в градусах равняется {:.5f}.'.format(alpha, alpha * 180 / pi))

t_sh = input('Введите шаг точности построения (по умолчанию - 0.1 c):')
if t_sh == '':
    t_sh = 0.1
t_sh = float(t_sh)

print('По последним известиям график представлен ниже:')

xList, yList = list(), list()
t0 = 0

while t0 < t:
    xList.append(x_t(v0, alpha, t0))
    yList.append(y_t(v0, alpha, t0))
    t0 += t_sh

pylab.plot(xList, yList)
pylab.show()
