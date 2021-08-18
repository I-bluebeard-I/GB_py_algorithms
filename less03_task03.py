"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""


from random import randint

a = [randint(-10, 100) for n in range(0, 20)]
min_idx = a.index(min(a))
max_idx = a.index(max(a))

print(f'Исходный список: {a}')
a[min_idx], a[max_idx] = a[max_idx], a[min_idx]
print(f'Конечный список: {a}')
