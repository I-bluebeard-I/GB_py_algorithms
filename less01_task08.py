"""
8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
"""


year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Високосный')
else:
    print('Не високосный')
