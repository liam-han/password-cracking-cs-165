from string import ascii_lowercase
from itertools import product


"""
for i in range(3):
    passwords = [''.join(letter) for letter in product(ascii_lowercase, repeat = i+2)]
    print(passwords)"""

def bit_string(string):
    x = ' '.join(format(ord(x), 'b') for x in string)

    return x


def bit_int(number):
    b = '{0:04b}'.format(number)
    bit_len = len(b)
    bits = [(number >> bit) & 1 for bit in range(bit_len - 1, -1, -1)]
    
    return b


x = '6'

if isinstance(x, int):
    some = bit_int(x)
if isinstance(x, str):
    some = bit_string(x)

print(some)

example = [1,2,4,5]

for i, e in enumerate(example):
    print(i)
    print(e)