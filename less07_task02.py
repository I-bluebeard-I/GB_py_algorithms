"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""


from random import randint


def merge_sort(ary):
    if len(ary) == 1 or len(ary) == 0:
        return ary

    left, right = ary[:len(ary) // 2], ary[len(ary) // 2:]
    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    ary_tmp = (len(left) + len(right)) * [0]
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ary_tmp[k] = left[i]
            i += 1
        else:
            ary_tmp[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        ary_tmp[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        ary_tmp[k] = right[j]
        j += 1
        k += 1
    for i in range(len(ary)):
        ary[i] = ary_tmp[i]
    return ary


a = []
for i in range(10):
    a.append(randint(0, 50))
print(f'Массив до сортировки: {chr(9)*2}{a}')
print(f'Массив после сортировки: {chr(9)}{merge_sort(a)}')
