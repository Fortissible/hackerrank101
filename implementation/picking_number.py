#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a_dic = {}
    res_max = 0
    prev_val = 0
    prev_key = 0
    for item in a:
        if item in a_dic.keys():
            a_dic[item] += 1
        else:
            a_dic[item] = 1
    myKeys = list(a_dic.keys())
    myKeys.sort()
    sorted_dict = {i: a_dic[i] for i in myKeys}
    for idx, i in enumerate(sorted_dict):
        if len(sorted_dict) == 1:
            res_max = sorted_dict[i]
        if idx != 0:
            if sorted_dict[i] + prev_val >= res_max and abs(prev_key-i) <= 1:
                res_max = sorted_dict[i] + prev_val
            elif sorted_dict[i] >= res_max:
                res_max = sorted_dict[i]
        prev_val = sorted_dict[i]
        prev_key = i
    return res_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()