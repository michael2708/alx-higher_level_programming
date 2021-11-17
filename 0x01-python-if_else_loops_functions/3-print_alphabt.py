#!/usr/bin/python3
for c in range(ord('a'), ord('a')+26):
    if chr(c) == "q" or chr(c) == "e":
        continue
    else:
        print('{}'.format(chr(c)), end='')
