#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    list_s = list(s)
    res = 0
    for idx in range(0, len(list_s), 3):
        if list_s[idx] != "S":
            res += 1
        if list_s[idx+1] != "O":
            res += 1
        if list_s[idx+2] != "S":
            res += 1
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()