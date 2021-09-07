"""
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""


s = 'Process finished with exit code 0'
dictionary = {}

for i in range(len(s)):
    n = s[i: len(s) - (len(s) - i) + 1]
    if dictionary.get(n) is not None:
        dictionary[n] += 1
    else:
        dictionary.setdefault(n, 1)




i = 0
while i <= len(dictionary):
    for k, v in dictionary.items():
        if v == i + 1:
            print(f'{k}: {v}')
    i += 1
