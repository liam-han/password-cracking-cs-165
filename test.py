from string import ascii_lowercase
from itertools import product


"""
for i in range(3):
    passwords = [''.join(letter) for letter in product(ascii_lowercase, repeat = i+2)]
    print(passwords)"""

=

def convert_to_binary(string):
    return {
        '0': "0000",
        '1': "0001",
        '2': "0010",
        '3': "0011",
        '4': "0100",
        '5': "0101",
        '6': "0110",
        '7': "0111",
        '8': "1000",
        '9': "1001",
        'a': "1010",
        'b': "1011",
        'c': "1100",
        'd': "1101",
        'e': "1110",
        'f': "1111"

    }[string]

x = convert_to_binary('a')
print(x)