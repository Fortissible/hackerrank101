#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    res = 0
    req_char = 0
    char_list = list(password)
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    criteria_chckmark = [0, 0, 0, 0, 0] #is6Length, isNum, isLow, isHigh, isSpecial
    for char in char_list:
        criteria_chckmark[0] = len(password)
        if char in numbers:
            criteria_chckmark[1] = 1
        if char in lower_case:
            criteria_chckmark[2] = 1
        if char in upper_case:
            criteria_chckmark[3] = 1
        if char in special_characters:
            criteria_chckmark[4] = 1
            
    for idx in range(1, len(criteria_chckmark)):
        if criteria_chckmark[idx] == 0:
            req_char += 1
            
    if criteria_chckmark[0] >= 6:
        res = req_char
    else:
        if 6-criteria_chckmark[0] >= req_char:
            res = 6-criteria_chckmark[0]
        else:
            res = req_char
    print(criteria_chckmark)
    print(req_char)
    print(res)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()