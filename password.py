from itertools import product
from string import ascii_lowercase
for i in range(6):
    keywords = [''.join(letter) for letter in product(ascii_lowercase, repeat = i+2)]
    print(keywords)





