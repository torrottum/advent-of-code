#!/usr/bin/env python3
import os

with open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt') as f:
    p1 = 0
    p2 = 0
    s = 0
    for line in f.readlines():
        line = line.rstrip()
        if line == '':
            continue

        words = line.split(' ')
        if len(words) == len(set(words)):
            p1 += 1

        x=[''.join(sorted(i)) for i in line.split(' ')]
        if len(x) == len(set(x)):
            p2 += 1

    print('Part 1: {}'.format(p1))
    print('Part 2: {}'.format(p2))
