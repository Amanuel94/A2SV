#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    i = 0
    count = 0
    while i < len(a):
        j = 0
        while j <= len(a)-2:
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1], a[j]
                count+=1
            j+=1
        i+=1
    print("Array is sorted in " + str(count) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
nHR
