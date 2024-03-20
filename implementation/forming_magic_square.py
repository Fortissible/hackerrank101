#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
def generateAllMagicSquare():
    mtxMgc = [
        [6, 1, 8],
        [7, 5, 3],
        [2, 9, 4]
    ]
    all_squares = [mtxMgc]
    all_squares.append(mtxMgc[::-1])
    all_squares.append([i[::-1] for i in mtxMgc])
    all_squares.append(all_squares[2][::-1])
    temp_squares = []
    for i in range(len(s)):
        temp = []
        for j in range(len(s)):
            temp.append(mtxMgc[j][i])
        temp_squares.append(temp)
    all_squares.append(temp_squares)
    all_squares.append(all_squares[4][::-1])
    all_squares.append([i[::-1] for i in all_squares[4]])
    all_squares.append(all_squares[6][::-1])
    return all_squares

def formingMagicSquare(s):
    all_solution_spaces = generateAllMagicSquare()

    least = 99
    for i in all_solution_spaces:
        temp = 0
        for j in range(3):
            for k in range(3):
                temp += abs(s[j][k]-i[j][k])
        if temp < least:
            least = temp

    return least

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()