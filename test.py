from multiprocessing import Pool, cpu_count
import time
from itertools import product
from string import ascii_lowercase
import multiprocessing



def program(n):
    counter = 0
    for letter in product(ascii_lowercase, repeat = n):
        password = ''.join(letter) 
        counter += 1

        print(password)
    return password

def f(n):
    for letter in product(ascii_lowercase, repeat = n):
        password = ''.join(letter) 
        if password == 'bbbbb':
            break
        print(password)
    return password

if __name__ == '__main__':
   start = time.time()
   for k in range(1):
        #pool = Pool(10)
        print(multiprocessing.cpu_count())
       
        pool = Pool(multiprocessing.cpu_count())
        pool.map_async(program, range(2,3))
        pool.close()
        pool.join()
   print(multiprocessing.cpu_count())

   end = time.time()
   print(end-start)
