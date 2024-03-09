#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    upper_char = [65, 90]
    lower_char = [97, 122]
    caesar_cipher = []
    for char in list(s):
        if ord(char) in range(upper_char[0], upper_char[1]+1):
            print(char, ord(char), chr(ord(char)))
            caesr = ord(char) + (k % 26)
            if caesr > upper_char[1]:
                caesr = 65 + caesr - upper_char[1] -1
            print(caesr, chr(caesr))
            caesar_cipher.append(chr(caesr))
        elif ord(char) in range(lower_char[0], lower_char[1]+1):
            print(char, ord(char), chr(ord(char)))
            caesr = ord(char) + (k % 26)
            if caesr > lower_char[1]:
                caesr = 97 + caesr - lower_char[1] -1
            print(caesr, chr(caesr))
            caesar_cipher.append(chr(caesr))
        else:
            caesar_cipher.append(char)
    return ''.join(caesar_cipher)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()