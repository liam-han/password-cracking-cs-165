import random
import threading
from itertools import product
from string import ascii_lowercase
import time

start = time.time()
for i in range(4):
    for letter in product(ascii_lowercase, repeat = i+1):
        password = ''.join(letter) 
        print(password)

end = time.time()
print(end-start)