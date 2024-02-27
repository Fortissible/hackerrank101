#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    min_cost = 0
    multiplier = 0
    rev_sorted_cost = sorted(c, reverse=True)
    sorted_cost = sorted(c)
    if k >= len(sorted_cost):
        for cost in sorted_cost:
            min_cost += cost
    else:
        for idx, cost in enumerate(rev_sorted_cost):
            print(f"CURRENT MULTIPLIER {multiplier}")
            print(f"COST OF TYPE {idx+1} FLOWER IS {cost} WITH MULTIPLIER IS {(multiplier+1)*cost}")
            min_cost += (multiplier+1)*cost
            print(f"TOTAL MIN_COST {min_cost}")
            multiplier = (idx+1)//k
    return min_cost
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()