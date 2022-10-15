import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.


def plusMinus(arr):
    # Write your code here
    pos=0
    neg=0
    zer=0
    for values in arr:
        if values>0:
         pos=pos+1
         
        elif values<0:
            neg=neg+1
         
        else:
            zer=zer+1
            
        length=len(arr)
    print ("{:.6f}".format(pos/length))
    print ("{:.6f}".format(neg/length))
    print ("{:.6f}".format(zer/length))
       

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
