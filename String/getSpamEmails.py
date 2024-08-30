#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getSpamEmails' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY subjects
#  2. STRING_ARRAY spam_words
#

def getSpamEmails(subjects, spam_words):
    resultarr = ["not_spam"] * len(subjects)
    dspam_words = {}

    for sword in spam_words:
        if sword.lower() not in dspam_words:
            dspam_words[sword.lower()] = 1

    for i in range(0, len(subjects)):
        line = subjects[i].lower().split(" ")
        dwords = {}
        for word in line:
            if word in dwords:
                dwords[word] += 1
            else:
                dwords[word] = 1

        count = 0

        for spamword in dspam_words:
            if spamword in dwords:
                count += 1
                if dwords[spamword] >= 2:
                    resultarr[i] = "spam"
                if count >= 2:
                    resultarr[i] = "spam"

    return resultarr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    subjects_count = int(input().strip())

    subjects = []

    for _ in range(subjects_count):
        subjects_item = input()
        subjects.append(subjects_item)

    spam_words_count = int(input().strip())

    spam_words = []

    for _ in range(spam_words_count):
        spam_words_item = input()
        spam_words.append(spam_words_item)

    result = getSpamEmails(subjects, spam_words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
