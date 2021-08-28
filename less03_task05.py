"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.
"""


from random import randint

a = [randint(-10, 5) for n in range(0, 20)]
print(a)
sorted_a = sorted(a)

zero_idx = None
for n in range(len(sorted_a)-1):
    if sorted_a[n] >= 0:
        zero_idx = n
        break

mx = max(sorted_a[0:zero_idx])
max_idx = a.index(mx)
print(f'максимальный отрицательный элемент = {mx}\n'
      f'индекс в массиве: {max_idx}')
