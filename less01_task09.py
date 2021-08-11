"""
9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""


from statistics import mean

num_1 = int(input('Введите число 1: '))
num_2 = int(input('Введите число 2: '))
num_3 = int(input('Введите число 3: '))

minimum = float('inf')
num_list = [num_1, num_2, num_3]
num_avg = mean(num_list)
print(min(num_list, key = lambda x: abs(x-num_avg)))
