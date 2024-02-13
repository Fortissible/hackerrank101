#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

# n m s        m-(n-s+1)
# 5 2 1 => 2    -3
# 7 19 2 => 6    13
# 3 7 3 => 3    6
# 4 8 1 => 4    4
# 8 6 3 => 8   0

def saveThePrisoner(n, m, s):
    is_rounded = m-(n-s+1)
    if is_rounded > 0:
        return n if is_rounded % n == 0 else is_rounded % n
    else:
        return n if s+m-1 == 0 else s+m-1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()