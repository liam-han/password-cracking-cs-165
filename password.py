from itertools import product
from string import ascii_lowercase
from hashlib import md5


# team47:$1$hfT7jp2q$DbF6xvgpiK3Nu1un54h3V1:16653:0:99999:7:::

salt = 'hfT7jp2q'
hashh = 'DbF6xvgpiK3Nu1un54h3V1'
magic = "$1"


def ascii(string):
    ascii_code = ''.join(str(ord(ch)) for ch in string)

    return ascii_code


for i in range(2):
    passwords = [''.join(letter) for letter in product(ascii_lowercase, repeat = i+2)]
    for password in passwords:
        print(password)
        alternate_sum = md5(password + salt + password)
        print(alternate_sum)




