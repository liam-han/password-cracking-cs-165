from string import ascii_lowercase
from itertools import product



for i in range(1):
    passwords = [''.join(letter) for letter in product(ascii_lowercase, repeat = i+1)]
    print(passwords)


print('ok')
print('ok')
print('ok')
print('ok')
print('ok')
print('ok')
print('ok')
print('ok')


