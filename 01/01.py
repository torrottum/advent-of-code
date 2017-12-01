#!/usr/bin/env python3

import os

def sum_digits(digits, part_one = True):
    s = 0
    step = 1
    if not part_one:
        step = int(len(digits) / 2)

    for i in range(len(digits)):
        j = i + step

        if j >= len(digits):
            j = 0
            if not part_one:
                j = i - step

        if digits[i] == digits[j]:
            s += int(digits[i])
    return s

with open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt') as f:
    digits = f.read().rstrip()
    print('Part one', sum_digits(digits))
    print('Part two', sum_digits(digits, False))