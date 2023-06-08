#!/usr/bin/python3

import sys
from calculator_1 import mul, sub, add, div

def calculate(a, op, b):
    dic = {"+": add, "-": sub, "*": mul, "/": div}

    if op not in dic:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    return dic[op](a, b)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    result = calculate(a, op, b)
    print("{} {} {} = {}".format(a, op, b, result))
