from itertools import product
from string import ascii_lowercase
from hashlib import md5
import time
import threading
from multiprocessing.dummy import Pool
import random
from multiprocessing import Process





# team47:$1$hfT7jp2q$DbF6xvgpiK3Nu1un54h3V1:16653:0:99999:7:::


encrypted = "u6EkeePAlgl3wYcJ56O9o."
salt = "hfT7jp2q"
magic = "$1$"
base_64 = './0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
order = [11,4,10,5,3,9,15,2,8,14,1,7,13,0,6,12]
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def ascii(string):
    #ascii_code = ':'.join(str(ord(ch)) for ch in string)
    ascii_code = ":".join("{:02x}".format(ord(c)) for c in string)  

    return ascii_code


def bit_int(number):
    b = '{0:04b}'.format(number)
    bit_len = len(b)
    bits = [(number >> bit) & 1 for bit in range(bit_len - 1, -1, -1)]
    
    return b

def four(password, length):
    x = int(bit_int(length))
    x = (str(x))
    x = x[::-1]
    string = '' 
    letter = password[0]
    for c in x:
        if c == '1':
            string += chr(0)
        if c == '0':
            string += 'a'
    return string

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


def password(num):
        letters = []
        letters = num
        counter = 0
        for i in range(3):
                for letter in product(letters, repeat = i+1):
                        password = ''.join(letter) 
                        
                        counter+=1
                        #password = 'abcdef'

                        alternate_sum = md5(password + salt + password).digest()
                        x = ":".join("{:02x}".format(ord(c)) for c in alternate_sum) 
                        len1 = len(password)
                        len2 = len(alternate_sum)
                        if len1 < len2:
                                l = alternate_sum[:len1]

                        else:
                                l = (alternate_sum*5)[:len1]
                        init5 = four(password, len1)
                        
                        #combine = ascii(password + magic + salt + l + init5)
                

                        intermediate_sum_0 = md5(password + magic + salt + l + init5).digest()
                        t = ":".join("{:02x}".format(ord(c)) for c in intermediate_sum_0)
                        
                        intermediate_sum = list()
                        intermediate_sum.append(intermediate_sum_0)
                        for i in range(1000):
                                int_sum = ''
                                if i%2 == 0:
                                        int_sum += intermediate_sum[i]
                                if i%2 != 0:
                                        int_sum += password
                                if i%3 != 0:
                                        int_sum += salt
                                if i%7 != 0:
                                        int_sum += password
                                if i%2 == 0:
                                        int_sum += password
                                if i%2 != 0:
                                        int_sum += intermediate_sum[i]
                                
                                intermediate_sum.append(md5(int_sum).digest())

                        intermediate_sum_1000 = ascii(intermediate_sum[-1])
                        #print(intermediate_sum_1000)
                        final = ':'.join("{:02x}".format(ord(c)) for c in intermediate_sum[-1])
                        
                        final = final.split(':')
                
                        new_final = [None] * 16
                        for i, o in enumerate(order):
                                new_final[i] = final[o]

                        new_list = ''
                        new_list = new_list.join(new_final)
                        bits = ''
                        for c in new_list:
                                bits += convert_to_binary(c)

                        o = []
                        while bits:
                                o.append(bits[-6:])
                                bits = bits[:-6]

                        pw = []
                        for each in o:
                                fuck = int(each, 2)
                                pw.append(base_64[fuck])
                        new_pw = ''
                        new_pw = new_pw.join(pw)
                        #print(new_pw)
                        if new_pw == encrypted:
                                print('\n')
                                print("THE PASSWORD IS: " + new_pw)
                                print(new_pw)
                                print(new_pw)
                                print(new_pw)
                                print(new_pw)
                                print(new_pw)
                                print(new_pw)
                                print(new_pw)
                                quit()


"""if __name__ == "__main__": 
        t1 = threading.Thread(target=password, args=(2, )) 
        t2 = threading.Thread(target=password, args=(3, ))
        t1.start()
        start = time.time()
        t2.start()
        # wait until thread 1 is completely executed 
        t1.join()  
        #t2.join() 

        end = time.time()
        print('time: ')
        print(end - start)
        print('\n')
        print('Passwords per second: ')
        #print(counter/(end-start))
        
        # both threads completely executed 
        print("Done!")


#print(len(passwords))"""


if __name__ == '__main__':
        start = time.time()
        letters_2 = []
        letters_2.append(letters)
        for x in range(26):
                letters.insert(0, letters.pop())
               # print(letters)
                letters_2.append(letters)
        print(letters_2[2])
        for i in range(26):
                p = Process(target=password, args=(letters_2[i],))
                print(letters_2[2])
                p.start()
        p.join()
                
        end = time.time()
        print(end-start)