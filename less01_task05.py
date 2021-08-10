"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""


alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

alpha_1 = input('').lower()
alpha_2 = input('').lower()


try:
    if alphabet_ru.index(alpha_1) != ValueError:
        a1 = alphabet_ru.index(alpha_1) + 1
        a2 = alphabet_ru.index(alpha_2) + 1
except ValueError:
    try:
        if alphabet_en.index(alpha_1) != ValueError:
            a1 = alphabet_en.index(alpha_1) + 1
            a2 = alphabet_en.index(alpha_2) + 1
    except ValueError:
        pass

print(a1)
print(a2)
print(a2 - a1)
