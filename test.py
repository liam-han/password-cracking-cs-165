from string import ascii_lowercase
from itertools import product


"""
for i in range(3):
    passwords = [''.join(letter) for letter in product(ascii_lowercase, repeat = i+2)]
    print(passwords)"""

def bit_string(string):
    x = ' '.join('{0:08b}'.format(ord(x), 'b') for x in string)

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
testing = [None] * 16
for i, e in enumerate(example):
    print(i)
    print(e)

test = bit_string('abcd')
print(test)

fuck = int('0011', 2)
print(fuck)

base_64 = './0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
print(len(base_64))

s = '1234567890'
o = []
while s:
    o.append(s[-2:])
    s = s[:-2]
print(o)

3fb1f8623a46b7bf
b8173c38cb9eb7b5

