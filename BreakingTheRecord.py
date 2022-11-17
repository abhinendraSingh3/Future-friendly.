#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    # Write your code here
    if len(scores)<=0:
        return []
    else:
        low=scores[0]
        high=scores[0]
        result=[0,0]
        for i in scores:
             if i<low:
                 low=i
                 result[1]+=1
             elif i>high:
                 high=i
                 result[0]+=1
        return result    
               

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
 
