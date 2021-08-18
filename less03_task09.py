"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""


from random import randint

width = 7
height = 5

# Заполняем матрицу
a = []
for i in range(height):
    b = []
    for j in range(width):
        b.append(randint(1, 20))
        print(b[j], chr(9), end='')
    a.append(b)
    print()

# Ищем минимальные значения по столбцам
b = []
for i in range(width):
    min_j = float('inf')
    for j in range(height):
        min_j = min(min_j, a[j][i])
    b.append(min_j)

print(f'----------------------------\nmin = {b}')
print(f'{max(b) = }')
