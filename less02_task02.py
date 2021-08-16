"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


num = input('Введите число: ')

if num.isdigit():
    even = '02468'
    odd = '13579'
    even_quantity = 0
    odd_quantity = 0

    for n in num:
        if even.find(n) != -1:
            even_quantity += 1
        elif odd.find(n) != -1:
            odd_quantity += 1
    print(f'Четных {even_quantity}, нечетных: {odd_quantity}')
else:
    print(f'"{num}" не является числом')
