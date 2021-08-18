"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""


from random import randint

a = [randint(0, 30) for n in range(0, 20)]

a = sorted(a)
min_idx = a.index(min(a))
max_idx = a.index(max(a))

print(f'{a}\n')
print(f'{min(a) = }, {min_idx = }, {a[min_idx + 1] = }')
print(f'{max(a) = }, {max_idx = }, {a[max_idx - 1] = }')

s = 0
for n in range(min_idx + 1, max_idx - 1):
    s += a[n]

print(f'\nСумма элеметов между min / max: {s}')
