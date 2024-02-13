#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    bird_sightings = {}
    for a in arr:
        if a in bird_sightings:
            bird_sightings[a] += 1
        else:
            bird_sightings[a] = 0
    sorted_sightings = sorted(bird_sightings.items(), key=lambda x: x[1], reverse=True)
    min_id = 99
    prevs_id_cnt = -1
    for idx, item in enumerate(sorted_sightings):
        print(item)
        if item[1] >= prevs_id_cnt:
            if item[0] < min_id:
                min_id = item[0]
            prevs_id_cnt = item[1]
        else:
            break
    return min_id
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
