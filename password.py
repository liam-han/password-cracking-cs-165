from itertools import product
from string import ascii_lowercase
from hashlib import md5


# team47:$1$hfT7jp2q$DbF6xvgpiK3Nu1un54h3V1:16653:0:99999:7:::

salt = 'hfT7jp2q'
hashh = 'DbF6xvgpiK3Nu1un54h3V1'
magic = "$1$"


def ascii(string):
    #ascii_code = ':'.join(str(ord(ch)) for ch in string)
    ascii_code = ":".join("{:02x}".format(ord(c)) for c in string)  

    return ascii_code

def bit(number):
    b = '{0:04b}'.format(number)
    bit_len = len(b)
    print(b)
    bits = [(number >> bit) & 1 for bit in range(bit_len - 1, -1, -1)]
    
    return b

def four(password, length):
    x = int(bit(length))
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
        """print(password)
        x = ":".join("{:02x}".format(ord(c)) for c in password)
        print(x) """

        alternate_sum = md5(password + salt + password).digest()
        x = ":".join("{:02x}".format(ord(c)) for c in alternate_sum) 
        len1 = len(password)
        len2 = len(alternate_sum)
        if len1 < len2:
                l = alternate_sum[:len1]

        else:
                l = (alternate_sum*5)[:len1]
        init5 = four(password, len1)
        print(init5)
        combine = ascii(password + magic + salt + l + init5)
        print("combine")
        print(combine)  

        intermediate_sum = md5(password + magic + salt + l)
        '''for i in range(1000):
                if i%2 ==  0:
                        temporary = 
                if i%3 != 0:
        '''
