#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'missingWords' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def missingWords(s, t):
    missingres = []
    src = s.split(" ")
    tgt = t.split(" ")

    i, j = 0, 0

    while i < len(src) and j < len(tgt):
        if src[i] == tgt[j]:
            j += 1
        else:
            missingres.append(src[i])
        i += 1

    while i < len(src):
        missingres.append(src[i])
        i += 1

    return missingres
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    result = missingWords(s, t)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
