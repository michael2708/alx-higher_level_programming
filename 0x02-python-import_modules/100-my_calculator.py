#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        operator = {"+": add(a, b),
                    "-": sub(a, b),
                    "*": mul(a, b),
                    "/": div(a, b)}
        if op in operator:
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, operator[op]))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
