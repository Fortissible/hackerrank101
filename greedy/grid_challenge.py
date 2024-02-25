#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

# Creating a function for insertion sort algorithm
def insertion_sort(list1):
    # Outer loop to traverse on len(list1)
    for i in range(1, len(list1)):
   
        a = list1[i]
   
        # Move elements of list1[0 to i-1],
        # which are greater to one position
        # ahead of their current position
        j = i - 1
           
        while j >= 0 and a < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
                 
        list1[j + 1] = a
             
    return list1

def gridChallenge(grid):
    new_grid = []
    for g in grid:
        new_grid.append(insertion_sort(list(g)))
    for cidx in range(len(new_grid[0])):
        prev = new_grid[0][cidx]
        for ridx in range(1, len(new_grid)):
            if prev <= new_grid[ridx][cidx]:
                prev = new_grid[ridx][cidx]
            else:
                return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()