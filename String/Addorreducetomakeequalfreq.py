#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balanceContent' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING content as parameter.
#
from collections import Counter


def balanceContent(content):
    # Step 1: Count the frequency of each character
    print(content)
    char_count = Counter(content)

    # Get the list of frequencies of the characters
    frequencies = list(char_count.values())

    # Step 2: Try to make all frequencies equal to a target frequency
    # We will try to balance to each possible frequency between 1 and max(frequencies)
    min_operations = float('inf')

    # The possible frequencies to balance towards range from 1 to max(frequencies)
    for target_freq in range(1, max(frequencies) + 1):
        operations = 0

        # Calculate the number of operations needed to make each character's frequency match target_freq
        for freq in frequencies:
            if freq > target_freq:
                # Remove extra characters
                operations += freq - target_freq
            elif freq < target_freq:
                # Add missing characters
                operations += target_freq - freq

        # Update the minimum operations if this target frequency requires fewer operations
        min_operations = min(min_operations, operations)


    minvalue = min(frequencies)
    minvaluecount = frequencies.count(minvalue)
    print(min_operations,minvalue * minvaluecount)

    return min(min_operations,minvalue * minvaluecount)

if __name__ == '__main__':
    print(balanceContent("aaabbbc"))
    print(balanceContent("aabbc"))
    print(balanceContent("aaaaaabb"))
    print(balanceContent("aabbcdef"))
