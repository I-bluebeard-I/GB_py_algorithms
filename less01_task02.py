"""
2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
вправо и влево на два знака. Объяснить полученный результат.
"""


print('Логическое побитовое «И» над числами 5 и 6: ', format(5 & 6, 'b'))
print('Логическое побитовое «ИЛИ» над числами 5 и 6: ', format(5 | 6, 'b'))

print('Побитовый сдвиг влево на 2 знака числа 5: ', format(5 << 2, 'b'))
print('Побитовый сдвиг вправо на 2 знака числа 5: ', format(5 >> 2, 'b'))