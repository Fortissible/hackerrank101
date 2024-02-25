import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    sorted_arr = sorted(arr)
    res = -1
    for idx in range(len(sorted_arr)-k+1):
        sub_sorted_arr = sorted_arr[idx:idx+k]
        if res == -1:
            res = sub_sorted_arr[k-1]-sub_sorted_arr[0]
        elif sub_sorted_arr[k-1]-sub_sorted_arr[0] < res:
            res = sub_sorted_arr[k-1]-sub_sorted_arr[0]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()