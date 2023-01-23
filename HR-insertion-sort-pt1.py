#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, a):
    j = n - 1
    temp = a[n-1]
    while j > 0:
        
        if temp < a[j-1]:
            a[j] = a[j-1]
            print(" ".join(list(map(str, a))))
        else:
            a[j]  = temp
            break
        j-=1
    if j == 0 and temp <  a[0]:
        a[0] = temp
    elif j == 0:
        a[1] = temp
    print(" ".join(list(map(str, a))))
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
