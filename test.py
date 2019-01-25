from string import ascii_lowercase
from itertools import product


"""
for i in range(3):
    passwords = [''.join(letter) for letter in product(ascii_lowercase, repeat = i+2)]
    print(passwords)"""


def bit_int(number):
    b = '{0:04b}'.format(number)
    bit_len = len(b)
    bits = [(number >> bit) & 1 for bit in range(bit_len - 1, -1, -1)]
    
    return b


def bit_string(string):
    x =  ' '.join(format(ord(x), 'b') for x in string)

    return x
word = int('abcd')
x = bit_string(test)
print(x)

print(len(x))

y = bit_int(38)
print(y)