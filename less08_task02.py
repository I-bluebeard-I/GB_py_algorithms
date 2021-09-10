"""
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""


import heapq
from collections import Counter
from collections import namedtuple


# информация о вершинах
class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


# информация о листьях
class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


# encode
def encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)

    while len(h) > 1:
        freq1, count1, left = heapq.heappop(h)
        freq2, count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h != '':
        [(freq, count, root)] = h
        root.walk(code, '')

    # for ch in sorted(code):
    #     print(f'{ch}: {code[ch]}')
    return code


# decode
def decode(encoded, code):
    sx = []
    enc_ch = ''
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ''
                break
    return ''.join(sx)


# main
s = 'Do you like Python?'
code = encode(s)
encoded = ''.join(code[ch] for ch in s)

print(f'{s =}')
print(f'{encoded =}')
print(f'decode = {decode(encoded, code)}')
