def bit(number):
    b = '{0:04b}'.format(number)
    bit_len = len(b)
    print(b)
    bits = [(number >> bit) & 1 for bit in range(bit_len - 1, -1, -1)]
    
    return b

"""def setBitNumber(n): 
    if (n == 0): 
        return 0; 
  
    msb = 0; 
    while (n > 0): 
        n = int(n / 2); 
        msb += 1; 
  
    return (1 << msb); 
"""

def name(password, length)
    x = int(bit(6))
    x = (str(x))
    x = x[::-1]
    print(x)
    string = '' 
    letter = password[0]
    for c in x:
        print(c)
        if c == '1':
            string += chr(0)
            print(chr(0))
        if c == '0':
            string += 'a'
    return string


print(string)

ascii_code = ":".join("{:02x}".format(ord(c)) for c in string)
print(ascii_code)

'''x = bit(6)[::-1]
print(str(x) + 'asldkf')
y = setBitNumber(6)
g = bit(y)
print(g)
for x in range(y-1):
    for ch in str(x):
        if ch == 1:
            print(1)
        else:
            print(0)
'''
