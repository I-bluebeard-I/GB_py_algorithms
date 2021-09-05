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
#
#
# alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
# alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#
# alpha = int(input('Введите номер буквы в алфавите: ').lower())
#
# if alpha <= 26:
#     print(f'{alpha}-я буква в EN алфавите: {alphabet_en[alpha-1]}')
#     print(f'{alpha}-я буква в RU алфавите: {alphabet_ru[alpha-1]}')
# elif alpha <= 33:
#     print(f'{alpha}-я буква в RU алфавите: {alphabet_ru[alpha-1]}')
# else:
#     print('Введенный номер находятся за пределами RU-EN алфавита')
pass


# less03_task05
pass
# """
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.
# """
#
#
# from random import randint
#
# a = [randint(-10, 5) for n in range(0, 20)]
# print(a)
# sorted_a = sorted(a)
#
# zero_idx = None
# for n in range(len(sorted_a)-1):
#     if sorted_a[n] >= 0:
#         zero_idx = n
#         break
#
# mx = max(sorted_a[0:zero_idx])
# max_idx = a.index(mx)
# print(f'максимальный отрицательный элемент = {mx}\n'
#       f'индекс в массиве: {max_idx}')
pass


# less05_task02
pass
# def sum_func(first, second):
#     numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
#
#     if len(first) > len(second):
#         first, second = second, first
#
#     first = first[::-1]
#     second = second[::-1]
#     third = []
#
#     c = 0
#     for i in range(len(second)):
#         if i == len(first):
#             break
#         a = numbers.index(second[i])
#         b = numbers.index(first[i])
#         third.append(numbers[(a + b + c) % 16])
#         c = (a + b + c) // 16
#
#     diff = len(second) - len(first)
#     if diff:
#         for i in range(len(second[-diff:])):
#             third.append(numbers[(numbers.index(second[-diff + i]) + c) % 16])
#             c = (numbers.index(second[-diff + i]) + c) // 16
#     if c == 1:
#         third.append('1')
#
#     return third[::-1]
