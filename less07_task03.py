"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
сложно, то используйте метод сортировки, который не рассматривался на уроках
"""


from random import randint


# def median(data):
#     data = sorted(data)
#     print(data)
#     n = len(data)
#     if n == 0:
#         raise StatisticsError("no median for empty data")
#     if n % 2 == 1:
#         return data[n // 2]
#     else:
#         i = n // 2
#         return (data[i - 1] + data[i]) / 2
# print(f'Медиана: {median(a)}')


m = 5
a = []
for i in range(2 * m + 1):
    a.append(randint(-100, 100))
print(f'Массив до сортировки: {chr(9)}{a}')
print(f'Сортированный массив: {chr(9)}{sorted(a)}')

b = a.copy()
while len(b) > 1:
    c = 0
    i = 0
    mx = max(b)
    mn = min(b)
    if b.index(mn) > b.index(mx):
        mx, mn = mn, mx
    while i < (len(b)):
        if b[i] == mn:
            b = b[:i] + b[i+1:]
            mn = None
            c += 1
        if b[i] == mx:
            b = b[:i] + b[i+1:]
            mx = None
            c += 1
        if c == 2:
            break
        i += 1

print(f'Медиана: {b}')