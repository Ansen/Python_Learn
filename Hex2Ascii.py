''' Hex convert to ascii'''
import binascii

def str2list(list):
    for i in range(0,len(list)-1,2):
        print '%s%s '%(list[i], list[i+1]),
        

def Hex2ascii(char):
    value = []
    for i in range(len(char)):
        b = binascii.b2a_hex(char[i])
        b = chr(int(b))
        value.append(b)
    return value

a = '8A 67 5F 6C'
a = ''.join(a.split())
str2list(Hex2ascii(list(a)))
