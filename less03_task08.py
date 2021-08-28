"""
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""


from random import randint

width = 5
height = 4

# Заполняем матрицу
a = []
for i in range(height):
    b = []
    for j in range(width-1):
        b.append(randint(1, 20))
        print(b[j], chr(9), end='')
    b.append(None)
    a.append(b)
    print()
print()

# Считаем сумму по строкам
for i in range(height):
    a[i][width - 1] = sum(a[i][0: width - 1])

# Выводим итоговую матрицу
for i in range(height):
    for j in range(width):
        print(a[i][j], chr(9), end='')
    print()
