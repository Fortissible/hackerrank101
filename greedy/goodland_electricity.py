#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
def getBestNextPylon(placable_locs, best_loc, prev_pylon_loc, start):
    best_idx = -1
    for index, value in enumerate(placable_locs[start:]):
        if value <= prev_pylon_loc:
            continue
        if value > best_loc:
            break
        if value > prev_pylon_loc and value <= best_loc:
            best_idx = start + index
    return best_idx
        

def pylons(k, arr):
    placable_locs = [i for i in range(len(arr)) if arr[i] == 1] # All array indexes of 1
    prev_pylon_loc = -1
    last_covered_loc = -1
    best_next_loc = k-1
    total_pylon = 0
    start = 0
    while True:
        best_next_loc_idx = getBestNextPylon(placable_locs, best_next_loc, prev_pylon_loc, start)
        start = best_next_loc_idx + 1
        if best_next_loc_idx == -1:
            break
        else:
            prev_pylon_loc = placable_locs[best_next_loc_idx]
            last_covered_loc = placable_locs[best_next_loc_idx] + k - 1
            best_next_loc = last_covered_loc + k
            total_pylon += 1
    if total_pylon > 0 and last_covered_loc>=len(arr)-1:
        return total_pylon
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()