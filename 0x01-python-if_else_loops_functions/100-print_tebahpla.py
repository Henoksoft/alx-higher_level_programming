#!/usr/bin/python3
for c i range(ord('z'), ord('a') - 1, -1):
    if c % 2 != 0:
        c = c - ord(' ')
        print('{:s}'.format(chr(c)), end='')
