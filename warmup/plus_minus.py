#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    temp = [0, 0, 0]
    for element in arr:
        if (element > 0):
            temp[0] += 1
        elif (element < 0):
            temp[1] += 1
        else:
            temp[2] += 1
    for idx, val in enumerate(temp):
        print('%.6f' % (val/len(arr)))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
