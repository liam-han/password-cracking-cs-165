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

        combine = ascii(password + magic + salt + l)
        print(combine)
        