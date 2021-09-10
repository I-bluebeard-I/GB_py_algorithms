"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


def sum_func(first, second):
    numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

    if len(first) > len(second):
        first, second = second, first

    first = first[::-1]
    second = second[::-1]
    third = []

    c = 0
    for i in range(len(second)):
        if i == len(first):
            break
        a = numbers.index(second[i])
        b = numbers.index(first[i])
        third.append(numbers[(a + b + c) % 16])
        c = (a + b + c) // 16

    diff = len(second) - len(first)
    if diff:
        for i in range(len(second[-diff:])):
            third.append(numbers[(numbers.index(second[-diff + i]) + c) % 16])
            c = (numbers.index(second[-diff + i]) + c) // 16
    if c == 1:
        third.append('1')

    return third[::-1]
# -------------------------------------------------------------------------


def multi_func(first, second):
    numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    multi = '0'

    if len(first) > len(second):
        first, second = second, first

    first = first[::-1]
    second = second[::-1]

    for i in range(len(second)):
        third = []

        if i > 0:
            zero = 0
            while zero < i:
                third.append('0')
                zero += 1
        c = 0
        for j in first:
            a = numbers.index(second[i])
            b = numbers.index(j)
            third.append(numbers[(a * b + c) % 16])
            c = (a * b + c) // 16

            if j == len(first):
                break
        third.append(str(c))

        n2 = third[::-1]
        multi = sum_func(multi, n2)

    return(multi)


n1 = 'A2'
n2 = 'C4F'
print(sum_func(n1, n2))
print(multi_func(n1, n2))

# ['C', 'F', '1']
# ['7', 'C', '9', 'F', 'E']
