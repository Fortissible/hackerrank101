#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    all_char = list("abcdefghijklmnopqrstuvwxyz")
    for char in all_char:
        print(f"Check Char {char}")
        if char not in s:
            if char.upper() in s:
                continue
            else:
                return "not pangram"
    return "pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()