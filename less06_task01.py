"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность
вашей ОС.
"""

# less01_task06
pass
# """
# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# """


from pympler import tracker

tr = tracker.SummaryTracker()
alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

alpha = int(input('Введите номер буквы в алфавите: '))

if alpha <= 26:
    print(f'{alpha}-я буква в EN алфавите: {alphabet_en[alpha-1]}')
    print(f'{alpha}-я буква в RU алфавите: {alphabet_ru[alpha-1]}')
elif alpha <= 33:
    print(f'{alpha}-я буква в RU алфавите: {alphabet_ru[alpha-1]}')
else:
    print('Введенный номер находятся за пределами RU-EN алфавита')
tr.print_diff()
pass
# Расчет используемого объема памяти для Python 3.9, OS х64
# Исходная строка 'alphabet_en' = 37 + 26 = 63 байт
# Исходная строка 'alphabet_ru' = 37 + 33 = 70 байт
# 'alpha': int = 24 байта
# Как это коррелирует с данными tracker-a ниже - не ясно.
# -------------------------------------------------------------------------------------------------------------
#                   types |   # objects |   total size
# ======================= | =========== | ============
#                    list |        4275 |    370.27 KB
#                     str |        4272 |    297.65 KB
#                     int |         923 |     25.24 KB
#                    dict |           3 |    680     B
#                    code |           1 |    246     B
#   function (store_info) |           1 |    136     B
#                    cell |           2 |     80     B
#                 weakref |           1 |     72     B
#                  method |           1 |     64     B
#                   tuple |          -1 |   -136     B
# -------------------------------------------------------------------------------------------------------------


# less03_task05
pass
# """
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.
# """


from pympler import tracker
from random import randint

tr = tracker.SummaryTracker()
a = [randint(-10, 5) for n in range(0, 20)]

print(a)
sorted_a = sorted(a)

zero_idx = None

for n in range(len(sorted_a)-1):
    if sorted_a[n] >= 0:
        zero_idx = n
        break

mx = max(sorted_a[0:zero_idx])
max_idx = a.index(mx)
print(f'максимальный отрицательный элемент = {mx}\n'
      f'индекс в массиве: {max_idx}')
tr.print_diff()
pass
# Расчет используемого объема памяти для Python 3.9, OS х64
# Исходный список 'a' из 20 целых чисел: 24 * 20 (на целые числа) + 40 + 8 * 20 (список со ссылками) = 680 байт
# Список 'sorted_a' из 20 целых чисел: 24 * 20 (на целые числа) + 40 + 8 * 20 (список со ссылками) = 680 байт
# zero_idx: int = 24 байта
# n: int = 24 байта
# mx: int = 24 байта
# max_idx: int = 24 байта
#
# -------------------------------------------------------------------------------------------------------------
#                   types |   # objects |   total size
# ======================= | =========== | ============
#                    list |        4278 |    370.77 KB
#                     str |        4271 |    297.60 KB
#                     int |         929 |     25.41 KB
#                    dict |           3 |    400     B
#                    code |           1 |    246     B
#   function (store_info) |           1 |    136     B
#                    cell |           2 |     80     B
#                 weakref |           1 |     72     B
#                  method |           1 |     64     B
#                   tuple |          -2 |   -192     B
# -------------------------------------------------------------------------------------------------------------

# less05_task02
pass


def sum_func(first, second):
    numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

    if len(first) > len(second):
        first, second = second, first

    first = first[::-1]
    second = second[::-1]
    third = []

    c = 0
    for i in range(len(second)):
        if i == len(first):
            break
        a = numbers.index(second[i])
        b = numbers.index(first[i])
        third.append(numbers[(a + b + c) % 16])
        c = (a + b + c) // 16

    diff = len(second) - len(first)
    if diff:
        for i in range(len(second[-diff:])):
            third.append(numbers[(numbers.index(second[-diff + i]) + c) % 16])
            c = (numbers.index(second[-diff + i]) + c) // 16
    if c == 1:
        third.append('1')

    return third[::-1]


from pympler import tracker


tr = tracker.SummaryTracker()
first = 'A9BC'
second = '4FE16A'
print(sum_func(first, second))
tr.print_diff()

pass
# Расчет используемого объема памяти для Python 3.9, OS х64
# first: str = 37 + 4 = 41 байт
# second: str = 37 + 6 = 43 байта
# third: list из 6 символов: 37 + 6 (на символы) + 40 + 8 * 6 (список со ссылками) = 131 байт
# numbers: list из 6 символов: 37 + 16 (на символы) + 40 + 8 * 16 (список со ссылками) = 221 байт
# a: int = 24 байта
# b: int = 24 байта
# c: int = 24 байта
# i: int = 24 байта
# dif: int = 24 байта
#
# -------------------------------------------------------------------------------------------------------------
#                   types |   # objects |   total size
# ======================= | =========== | ============
#                    list |        4277 |    370.40 KB
#                     str |        4272 |    297.67 KB
#                     int |         922 |     25.21 KB
#                    dict |           3 |    400     B
#                    code |           1 |    246     B
#   function (store_info) |           1 |    136     B
#                    cell |           2 |     80     B
#                 weakref |           1 |     72     B
#                  method |           1 |     64     B
#                   tuple |          -2 |   -192     B
# -------------------------------------------------------------------------------------------------------------
