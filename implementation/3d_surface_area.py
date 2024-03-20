#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def search_some_surface(single_dim):
    res = 0
    for idx in range(len(single_dim)):
        if idx == 0:
            res += single_dim[idx]
        else:
            if single_dim[idx] - single_dim[idx-1] > 0:
                res += single_dim[idx] - single_dim[idx-1]
    return res

def surfaceArea(A):
    total_side = (len(A) * len(A[0])) * 2
    print(f"atas bawah: {total_side}")
    for i in A:
        total_side += search_some_surface(i)
        print(i)
    print(f"atas bawah depan: {total_side}")
    for i in A:
        total_side += search_some_surface(i[::-1])
        print(i[::-1])
    print(f"atas bawah depan belakang: {total_side}")
    for i in range(len(A[0])):
        total_side += search_some_surface([row[i] for row in A])
        print([row[i] for row in A])
    print(f"atas bawah depan belakang kiri: {total_side}")
    for i in range(len(A[0])):
        total_side += search_some_surface([row[i] for row in A[::-1]])
        print([row[i] for row in A[::-1]])
    print(f"atas bawah depan belakang kiri kanan: {total_side}")
    return total_side

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
