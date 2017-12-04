#!/usr/bin/env python3
import os

def check_phrase(words):
    l = len(words)
    x = l * -1
    for i in range(l):
        for j in range(l):
            if sorted(words[i]) == sorted(words[j]):
                x += 1
    return not x > 0

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

        if check_phrase(words):
            p2 += 1
            
    print('Part 1: {}'.format(p1))
    print('Part 2: {}'.format(p2))
