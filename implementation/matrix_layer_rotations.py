#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#
def matrixFraction(matrix, border, row, col, r, flat_dim):
    ring_arr = []
    for x in range(0+border, row-border):
        ring_arr.append(matrix[x][border])
                
    for y in range(0+border+1, col-border):
        ring_arr.append(matrix[row-border-1][y])
            
    for x in reversed(range(0+border, row-border-1)):
        ring_arr.append(matrix[x][col-border-1])
            
    for y in reversed(range(0+border+1, col-border-1)):
        ring_arr.append(matrix[border][y])
    
    new_arr = []
    for bef in range(flat_dim):
        new_idx = (bef-r) % flat_dim
        new_arr.append(ring_arr[new_idx])
    
    cnt = 0
    for x in range(0+border, row-border):
        matrix[x][border] = new_arr[cnt]
        cnt += 1
                
    for y in range(0+border+1, col-border):
        matrix[row-border-1][y] = new_arr[cnt]
        cnt += 1
            
    for x in reversed(range(0+border, row-border-1)):
        matrix[x][col-border-1] = new_arr[cnt]
        cnt += 1
            
    for y in reversed(range(0+border+1, col-border-1)):
        matrix[border][y] = new_arr[cnt]
        cnt += 1


def matrixRotation(matrix, r):
    row = len(matrix)
    col = len(matrix[0])
    anchor = 0
    if row % 2 == 0 and col % 2 == 0:
        if row // 2 > col // 2:
            anchor = col // 2
        else:
            anchor = row // 2
    elif row % 2 == 0:
        anchor = row//2
    else:
        anchor = col//2
    
    for border in range(anchor):
        flat_dim = (row-(border*2))*2 + (col-(border*2)-2)*2
        matrixFraction(matrix, border, row, col, r, flat_dim)
    
    for i_idx, i in enumerate(matrix):
        for j_idx, j in enumerate(i):
            if j_idx != col-1 or (i_idx == row-1 and j_idx == col-1):
                print(j, end=" ")
            else:
                print(j, end="\n")
        
            
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)