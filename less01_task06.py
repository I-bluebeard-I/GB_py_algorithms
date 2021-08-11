"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""


alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

alpha = int(input('').lower())

if alpha <= 26:
    print('alphabet_en', alphabet_en[alpha-1])
    print('alphabet_ru', alphabet_ru[alpha-1])
elif alpha <= 33:
    print('alphabet_ru', alphabet_ru[alpha-1])
else:
    print('-----')
