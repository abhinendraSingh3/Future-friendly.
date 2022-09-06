#!/bin/python3

import math
import os
import random
import re
import sys

def reverseArray(a): #this is the logic
    new_ar=[]
    while a:
      new_ar.append(a.pop())
    return new_ar
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
