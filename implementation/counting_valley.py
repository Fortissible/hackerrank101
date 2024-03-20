#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    res = 0
    isValley = 0
    altitude = 0
    for p in path:
        altitude = altitude + 1 if p == "U" else altitude - 1
        if (not isValley and altitude < 0):
            res += 1
            isValley = 1
        elif altitude >= 0:
            isValley = 0
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()