#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    res = 0
    for i in range(len(s)):
        cnt_tmp = 0
        length_tmp = 0
        for j in range(i, len(s)):
            cnt_tmp += s[j]
            length_tmp += 1
            if cnt_tmp == d and length_tmp == m:
                res += 1
                break
            elif cnt_tmp > d or length_tmp > m:
                break
    return res
                   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()