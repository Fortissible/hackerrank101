#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

# def missingNumbers(arr, brr):
#     a_idx = 0
#     res = []
#     for b_idx in range(len(brr)):
#         if brr[b_idx] != arr[a_idx]:
#             res.append(brr[b_idx])
#         elif a_idx != len(arr)-1:
#             a_idx += 1
#     return (sorted(list(set(res))))

def missingNumbers(arr, brr):
    a_idx = 0
    a_dic = {}
    b_dic = {}
    for b in brr:
        if a_idx != len(arr):
            if arr[a_idx] in a_dic:
                a_dic[arr[a_idx]] += 1
            else:
                a_dic[arr[a_idx]] = 1
            a_idx += 1
        if b in b_dic:
            b_dic[b] += 1
        else:
            b_dic[b] = 1
    print(a_dic)
    print()
    print(b_dic)
    res = []
    for b in b_dic:
        print(b)
        if b not in a_dic:
            print(f"{b} not in {a_dic}")
            res.append(b)
        elif b_dic[b] != a_dic[b]:
            print(f"{b}:{b_dic[b]} not equal to {b}:{a_dic[b]}")
            res.append(b)
    return sorted(list(set(res)))

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)
    
    print(result)