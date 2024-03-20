#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    truncated = s.replace(" ", "")
    sqrt_len = math.sqrt(len(truncated))
    row = int(math.floor(sqrt_len))
    col = int(math.ceil(sqrt_len))
    if (row*col < len(truncated)):
        row += 1
    
    enc_mtx = []
    for i in range(row):
        col_arr = []
        for j in range(col):
            if ((i*col)-1 + j < len(truncated)-1):
                col_arr.append(truncated[(i*col) + j])
            else:
                col_arr.append("null")
        enc_mtx.append(col_arr)
    
    print(enc_mtx)
    enc = ""
    for col in range(len(enc_mtx[0])):
        for row in range(len(enc_mtx)):
            if (enc_mtx[row][col] != "null"):
                enc += enc_mtx[row][col]
            else:
                continue
        if (col != len(enc_mtx[0])-1):
            enc += ' '
    
    return enc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()