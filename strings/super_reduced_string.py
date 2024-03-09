#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    print(len(s))
    str_list = list(s)
    reduced_idx = []
    cnt_del = 0
    for idx in range(len(str_list)-1):
        if str_list[idx] == str_list[idx+1]:
            reduced_idx.append(idx)
    print(reduced_idx)
    while len(reduced_idx) != 0:
        prevs_deleted = -1
        for del_idx in reduced_idx:
            print(f"del idx {del_idx}")
            if prevs_deleted != -1 and prevs_deleted == del_idx:
                continue
            if str_list[del_idx-cnt_del] == str_list[del_idx-cnt_del+1]:
                print(f"deleting chat at idx-{del_idx-cnt_del} and {del_idx-cnt_del+1}")
                str_list.pop(del_idx-cnt_del)
                str_list.pop(del_idx-cnt_del)
                prevs_deleted = del_idx+1
                cnt_del += 2
        reduced_idx = []
        cnt_del = 0
        for idx in range(len(str_list)-1):
            if str_list[idx] == str_list[idx+1]:
                reduced_idx.append(idx)
                
    if len(str_list) == 0:
        return "Empty String"
    else:
        return ''.join(str_list)

if __name__ == '__main__':
    print(superReducedString("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))