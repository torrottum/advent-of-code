#!/usr/bin/env python3
import os

def redistribute(banks):
    i = banks.index(max(banks))
    v = banks[i]
    n = i
    banks[i] = 0
    while v != 0:
        n += 1
        n = n % len(banks)
        banks[n] += 1
        v -= 1
    return banks

with open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt') as f:
    banks = [int(i) for i in f.read().split('\t')]
    seen = [banks[:]]
    curr = banks[:]

    s = 0
    times = 0
    while True:
        s+=1
        curr = redistribute(curr[:])
        if curr in seen:
            if times == 1:
                print('Part two: {}'.format(s), times)
                break
            seen = [curr[:]]
            s = 0
            times += 1
        else:
            seen.append(curr[:])
