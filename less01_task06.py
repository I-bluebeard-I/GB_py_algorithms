"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""


alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

alpha = int(input('Введите номер буквы в алфавите: ').lower())

if alpha <= 26:
    print(f'{alpha}-я буква в EN алфавите: {alphabet_en[alpha-1]}')
    print(f'{alpha}-я буква в RU алфавите: {alphabet_ru[alpha-1]}')
elif alpha <= 33:
    print(f'{alpha}-я буква в RU алфавите: {alphabet_ru[alpha-1]}')
else:
    print('Введенный номер находятся за пределами RU-EN алфавита')
