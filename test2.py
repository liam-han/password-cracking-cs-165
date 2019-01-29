import random
import threading
from itertools import product
from string import ascii_lowercase
import time
from collections import deque


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


'''def words(array):
	a = deque(letters)
	for i in range(3):
		new = a.rotate(1)
		array.append(new)
		a = new
	return array
aza = []
words = words(aza)
'''

def rotate(l):
    return l[-1:] + l[:-1]


mixed = []
for i in range(26):
	letters = rotate(letters)
	mixed.append(letters)

for mix in mixed:
	print(mix)