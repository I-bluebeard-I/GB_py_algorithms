"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""


alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

alpha_1 = input('Введите первую букву: ').lower()
alpha_2 = input('Введите вторую букву: ').lower()


try:
    if alphabet_ru.index(alpha_1) != ValueError:
        idx_alpha_1 = alphabet_ru.index(alpha_1) + 1
        idx_alpha_2 = alphabet_ru.index(alpha_2) + 1
except ValueError:
    try:
        if alphabet_en.index(alpha_1) != ValueError:
            idx_alpha_1 = alphabet_en.index(alpha_1) + 1
            idx_alpha_2 = alphabet_en.index(alpha_2) + 1
    except ValueError:
        print('Введенные символы находятся за пределами RU-EN алфавита')
        exit(0)

print(f'\nПорядковый номер буквы "{alpha_1}" в алфавите: {idx_alpha_1}')
print(f'Порядковый номер буквы "{alpha_2}" в алфавите: {idx_alpha_2}')
print(f'Между буквами "{alpha_1}" и "{alpha_2}" находится {idx_alpha_2 - idx_alpha_1 - 1} буква(ы)')
