#!/usr/bin/env python3
import os

def part_one(lines):
    s = 0
    for line in lines:
        s += max(line) - min(line)
    return s


def part_two(lines):
    s = 0
    for line in lines:
        for i in range(len(line)):
            for j in range(len(line)):
                if (line[i] == line[j]):
                    continue
                if (line[i] % line[j] == 0):
                    s += int(line[i] / line[j])
    return s

with open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt') as f:
    lines = []
    for line in f.readlines():
        lines.append(list(map(int, line.rstrip().split('\t'))))
    print('Part one: {}'.format(part_one(lines)))
    print('Part two: {}'.format(part_two(lines)))