"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

start_chr = 32
end_chr = 127
symb_count = start_chr

while symb_count <= end_chr:
    pair_count = 0
    while pair_count < 10 and symb_count <= end_chr:
        print(f'[ ascii({symb_count}), "{chr(symb_count)}" ]', end=chr(9))
        symb_count += 1
        pair_count += 1
    print()
