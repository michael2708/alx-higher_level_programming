#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if length == 1:
        print("0")
    else:
        sum = 0
        for c in range(1, length):
            sum += int(argv[c])
        print(sum)
