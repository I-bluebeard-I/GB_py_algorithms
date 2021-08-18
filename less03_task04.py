"""
Определить, какое число в массиве встречается чаще всего.
"""


from random import randint

a = [randint(10, 40) for n in range(0, 20)]

print(f'Исходный список: {chr(9)*4}{a}')
print(f'Сортированный исходный список: {chr(9)*1}{sorted(a)}')
print(f'Наиболее частый элемент в списке: {max(set(a), key=a.count)}')
