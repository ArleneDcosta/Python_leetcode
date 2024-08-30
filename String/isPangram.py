#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isPangram' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY pangram as parameter.
#

def isPangram(pangram):
    s = "abcdefghijklmnopqrstuvwxyz"
    resultarr = ["0"] * len(pangram)

    for i in range(0, len(pangram)):
        alplist = [0] * 26
        for letter in pangram[i].lower():
            if letter != " ":
                alplist[s.index(letter)] = 1

        flag = 1
        for val in alplist:
            if val == 0:
                flag = 0
                continue
        if flag:
            resultarr[i] = "1"

    res = ""
    for val in resultarr:
        res += val
    return res

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pangram_count = int(input().strip())

    pangram = []

    for _ in range(pangram_count):
        pangram_item = input()
        pangram.append(pangram_item)

    result = isPangram(pangram)

    fptr.write(result + '\n')

    fptr.close()
