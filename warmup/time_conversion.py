#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[8:] == "AM":
        if s[:2] == "12":
            return "00:"+s[3:8]
        else:
            return s[:8]
    elif s[8:] == "PM":
        if s[:2] == "12":
            return "12:"+s[3:8]
        else:
            hour = 12 + int(s[:2])
            return str(hour)+s[2:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()