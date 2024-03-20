#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    res = 0
    min = sys.maxsize
    max = -sys.maxsize - 1
    min_idx = 0
    max_idx = 0
    for idx, element in enumerate(arr):
        res += element
        if element > max:
            max = element
            max_idx = idx
        if element < min:
            min = element
            min_idx = idx
    print(f"{res-arr[max_idx]} {res-arr[min_idx]}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)