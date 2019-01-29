from multiprocessing import Pool, cpu_count
import time
from itertools import product
from string import ascii_lowercase
import multiprocessing
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

'''for letter in product(a, repeat = 3):
                        password = ''.join(letter) 
                        print(password)
'''
letters_2 = []
letters_2.append(letters)
for x in range(26):
    letters.insert(0, letters.pop())
    print(letters)
    letters_2.append(letters)


for letter in product(letters, repeat = 4):
    password = ''.join(letter) 
    print(password)