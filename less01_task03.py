"""
3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
b = (y1 * x2 - y2 * x1) / (x2 - x1)
"""


x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))

if x1 != x2:
    if y1 != y2 and x1 != x2:
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        print(f'y =  {k}x ' + '{:+}'.format(b))
    else:
        print(f'y = ' + '{:+}'.format(y1))
else:
    print('x1 == x2')
