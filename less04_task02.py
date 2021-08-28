"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить
в виде комментариев в файле с кодом.
"""


import cProfile

order_num = int(input('input num: '))
a = [n for n in range(2, order_num * 9)]


def simple_nums():
    print('Без использования «Решета Эратосфена»')

    b = []
    for i in range(2, len(a)):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            b.append(i)

    print(f'{b}, \n{b[order_num - 1]}')


def simple_num_ero():
    print('Используя алгоритм «Решето Эратосфена»')

    a = [n for n in range(0, order_num * 9)]
    a[1] = 0

    i = 2
    while i < len(a):
        if a[i] != 0:
            j = i * 2
            while j < len(a):
                a[j] = 0
                j += i
        i += 1

    b = []
    for i in range(len(a)):
        if a[i] != 0:
            b.append(a[i])

    print(f'{b}, \n{b[order_num - 1]}')

# input num: 2345
cProfile.run('simple_nums()')

# 2379 function calls in 1.524 seconds

# Ordered by: standard name
#
# ncalls  tottime percall cumtime percall filename: lineno(function)
#     1   0.000   0.000   1.524   1.524   < string >: 1( < module >)
#     1   1.523   1.523   1.524   1.524   less04_task02.py: 16(simple_nums)
#     1   0.000   0.000   1.524   1.524   {built - in method builtins.exec}
#     1   0.000   0.000   0.000   0.000   {built - in method builtins.len}
#     2   0.001   0.000   0.001   0.000   {built - in method builtins.print}
#  2372   0.001   0.000   0.001   0.000   {method 'append' of 'list' objects}
#     1   0.000   0.000   0.000   0.000   {method'disable'of'_lsprof.Profiler'objects}


cProfile.run('simple_num_ero()')

# 76498 function calls in 0.020 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.020    0.020 <string>:1(<module>)
#        1    0.013    0.013    0.020    0.020 less04_task02.py:31(simple_num_ero)
#        1    0.001    0.001    0.001    0.001 less04_task02.py:34(<listcomp>)
#        1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
#    74119    0.004    0.000    0.004    0.000 {built-in method builtins.len}
#        2    0.002    0.001    0.002    0.001 {built-in method builtins.print}
#     2372    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
