import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:len(arr)-1]),sum(arr[1:]))
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
