#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    a_factor = []
    correspond_count = []
    res = []
    a.sort()
    b.sort()
    for idx, i in enumerate(a):
        cnt = 1
        if idx == 0:
            while i * cnt <= 100:
                a_factor.append(i*cnt)
                correspond_count.append(1)
                cnt += 1
        else:
            for fac_idx, factor in enumerate(a_factor):
                if factor % i == 0:
                    print(f"pop idx {fac_idx} w fac {factor} and a {i}")
                    correspond_count[fac_idx] += 1
    
    print(a_factor)
    print(correspond_count)
    
    for fac_idx, factor in enumerate(a_factor):
        if correspond_count[fac_idx] == len(a):
            valid_res = len(b)
            valid_tmp = 0
            for j in b:
                if j % factor == 0:
                    valid_tmp += 1
            if valid_tmp == valid_res:
                res.append(factor)
            
    print(res)
    return len(res)
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()