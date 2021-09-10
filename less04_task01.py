"""
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""


# less02_task08.py
# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество
# вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

from random import randint
import cProfile

string = ''
for i in range(0, 10000000):
    string += str(randint(0, 10))

symbol = input('Введите цифру: ')


def symb_search_1():
    # вариант 1
    print(f'Цифра "{symbol}" повторяется в последовательности {string.count(symbol)} раз(а)')


def symb_search_2():
    # вариант 2
    count = 0
    for s in string:
        if s == symbol:
            count += 1
    print(f'Цифра "{symbol}" повторяется в последовательности {count} раз(а)')

# Введите цифру: 2

cProfile.run('symb_search_1()')

# Цифра "2" повторяется в последовательности 908049 раз(а)
#          6 function calls in 0.013 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.013    0.013 <string>:1(<module>)
#         1    0.000    0.000    0.013    0.013 less04_task01.py:21(symb_search_1)
#         1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.013    0.013    0.013    0.013 {method 'count' of 'str' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('symb_search_2()')

# Цифра "2" повторяется в последовательности 908049 раз(а)
#          5 function calls in 0.393 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.393    0.393 <string>:1(<module>)
#         1    0.393    0.393    0.393    0.393 less04_task01.py:26(symb_search_2)
#         1    0.000    0.000    0.393    0.393 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
