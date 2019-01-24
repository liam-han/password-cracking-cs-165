from itertools import product
from string import ascii_lowercase
from hashlib import md5


# team47:$1$hfT7jp2q$DbF6xvgpiK3Nu1un54h3V1:16653:0:99999:7:::

salt = 'hfT7jp2q'
hashh = 'DbF6xvgpiK3Nu1un54h3V1'
magic = "$1$"
base_64 = './0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
order = [11,4,10,5,3,9,15,2,8,14,1, 7, 13, 0, 6, 12]

def ascii(string):
    #ascii_code = ':'.join(str(ord(ch)) for ch in string)
    ascii_code = ":".join("{:02x}".format(ord(c)) for c in string)  

    return ascii_code

def bit_string(string):
    x = ''.join(('{0:08b}'.format(ord(x), 'b')) for x in string)

    return x


def bit_int(number):
    b = '{0:04b}'.format(number)
    bit_len = len(b)
    bits = [(number >> bit) & 1 for bit in range(bit_len - 1, -1, -1)]
    
    return b

def four(password, length):
    x = int(bit_int(length))
    x = (str(x))
    x = x[::-1]
    print(x)
    string = '' 
    letter = password[0]
    for c in x:
        if c == '1':
            string += chr(0)
        if c == '0':
            string += 'a'
    return string


for i in range(1):
    passwords = [''.join(letter) for letter in product(ascii_lowercase, repeat = i+2)]
    for password in passwords:
        password = 'abcdef'
        

        alternate_sum = md5(password + salt + password).digest()
        x = ":".join("{:02x}".format(ord(c)) for c in alternate_sum) 
        len1 = len(password)
        len2 = len(alternate_sum)
        if len1 < len2:
                l = alternate_sum[:len1]

        else:
                l = (alternate_sum*5)[:len1]
        init5 = four(password, len1)
        print(ascii(l))
        print(ascii(init5))
        combine = ascii(password + magic + salt + l + init5)
        print("combine")
        print(combine)  

        intermediate_sum_0 = md5(password + magic + salt + l + init5).digest()
        t = ":".join("{:02x}".format(ord(c)) for c in intermediate_sum_0)
        print(t)
        
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
        print(intermediate_sum_1000)
        final = ':'.join("{:02x}".format(ord(c)) for c in intermediate_sum[-1])
        final = final.split(':')
        p = ''
        p = p.join(final)
        print('this is final')
        print(p)
        new_final = [None] * 16
        for i, o in enumerate(order):
                new_final[i] = p[o]

        new_list = ''
        new_list = new_list.join(new_final)
        bits = bit_string(new_list)

        print(new_list)
        print(bits)
        n = 6
        '''six_bits = [bits[i:i+n] for i in range(0, len(bits), n)]'''
        o = []
        while bits:
                o.append(bits[-6:])
                bits = bits[:-6]
        print(o)
        pw = []
        for each in o:
                fuck = int(each, 2)
                pw.append(base_64[fuck])
        print(pw)

        '''final_string = []
        for c in new_final:
                print(c)
                x = bit_string(c)
                final_string.append(x)
        new_list = ''
        new_list = new_list.join(final_string)

        print(new_list)
        print(len(new_list))
        '''
