#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

import statistics


def interQuartile(values, freqs):
    new_list = []
    for i in range(len(values)):
        for j in range(freqs[i]):
            new_list.append(values[i])

    new_list = sorted(new_list)
    n = len(new_list)

    left = new_list[0:n // 2]
    right = new_list[n // 2 + 1:n + 1]

    q1 = statistics.median(left)
    q3 = statistics.median(right)

    print(float(round(q3 - q1, 1)))


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
