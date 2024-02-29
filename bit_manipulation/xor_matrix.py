#!/bin/python3

import os
import sys

#
# Complete the xorMatrix function below.
#
def xorMatrix(m, first_row):
    total_col = len(first_row)
    total_row = m
    cur_row_num = 2
    curr_row = first_row
    nextRow = []
    while cur_row_num <= total_row:
        for idx in range(total_col):
            if (idx <= total_col-2):
                nextRow.append(curr_row[idx] ^ curr_row[idx+1])
            else:
                nextRow.append(curr_row[idx] ^ curr_row[0])
        curr_row = nextRow.copy()
        nextRow = []
        print(f"generated row-{cur_row_num} is : {curr_row}")
        cur_row_num += 1
    return curr_row

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    first_row = list(map(int, input().rstrip().split()))

    last_row = xorMatrix(m, first_row)

    fptr.write(' '.join(map(str, last_row)))
    fptr.write('\n')

    fptr.close()