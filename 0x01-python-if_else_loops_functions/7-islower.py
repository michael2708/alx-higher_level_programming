#!/usr/bin/python3
def islower(c):
    for n in range(ord('a'), ord('z')+1):
        if n == ord(c):
            return True
    return False
