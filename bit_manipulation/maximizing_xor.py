#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#
def xorFunction(a, b):
    return a ^ b

def maximizingXor(l, r):
    max_res = -1
    for i in range(l, r+1):
        for j in range(l, r+1):
            tmp_res = xorFunction(i, j)
            if tmp_res >= max_res:
                max_res = tmp_res
    return max_res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()