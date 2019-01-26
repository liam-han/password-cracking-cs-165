from string import ascii_lowercase
from itertools import product



for i in range(6):
    for letter in product(ascii_lowercase, repeat = i+1):
        password = ''.join(letter) 
        print(password)