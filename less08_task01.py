"""
1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""


import hashlib

s = 'Process finished with exit code 0'
dictionary = {}
count = 0

for i in range(1, len(s)):
    for j in range(len(s) - i + 1):
        hsh = hashlib.sha1(s[j: j + i].encode('utf-8')).hexdigest()
        
        if dictionary.get(hsh) is not None:
            dictionary[hsh] += 1
        else:
            dictionary.setdefault(hsh, 1)
        count += 1
        
print(f'Всего подстрок: {count}')
print(f'Уникальных подстрок: {len(dictionary)}\n')

print('Повторяющиеся подстроки: ')
for k, v in dictionary.items():
    if v > 1:
        print(f'{k}: {v}')
