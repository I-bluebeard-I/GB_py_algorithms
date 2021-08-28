"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число
и сумму его цифр.
"""


print('Введите несколько натуральных чисел. Для окончания ввода чисел введите знак равенства"="')

count = 1
a = {}

while True:
    b = input(f'Введите число {count}: ')
    if b == '=':
        break
    else:
        if b.replace('-', '').replace(' ', '').isdigit():
            a.setdefault(b.replace('-', '').replace(' ', ''))
            count += 1
        else:
            print(f'"{b}" не является числом и не будет учтено, повторите ввод')
print(f'Вы ввели {count-1} чис(ел/ла): ', *a.keys())

# a = {2343: None, 76756: None, 34: None, 56789: None, 98: None, 9997: None}
a_sum_of_digit = []

for num in a:
    sum_of_digit = 0
    for n in str(num):
        sum_of_digit += int(n)
    a[num] = sum_of_digit
print(f'Наибольшее число по сумме цифр: {list(a.keys())[list(a.values()).index(max(a.values()))]} ,'
      f'Сумма цифр: {max(a.values())}')
