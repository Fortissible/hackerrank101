#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    list_s = list(s)
    
    for idx in range(len(list_s)-1):
        asc_s1 = ord(list_s[idx])
        asc_s2 = ord(list_s[idx+1])
        asc_r1 = ord(list_s[len(list_s)-1-idx])
        asc_r2 = ord(list_s[len(list_s)-2-idx])
        if abs(asc_s1-asc_s2) == abs(asc_r1-asc_r2):
            continue
        else:
            return "Not Funny"
    return "Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()