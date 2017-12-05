#!/usr/bin/env python3
import os

def p1(maze):
    i = 0
    s = 0
    while i >= 0 and i < len(maze):
        v = maze[i]
        maze[i] += 1
        i += v
        s += 1
    return s

def p2(maze):
    i = 0
    s = 0
    while i >= 0 and i < len(maze):
        v = maze[i]
        if v >= 3:
            maze[i] -= 1
        else:
            maze[i] += 1
        i += v
        s += 1
    return s

with open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt') as f:
    maze =  [int(i.strip()) for i in f.readlines()]
    maze2 = maze[:]
    print('Part 1: {}'.format(p1(maze)))
    print('Part 2: {}'.format(p2(maze2)))
