#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import *
    argv = sys.argv[1:]
    i = 1
    sum = 0
    operators = ["+", "-", "*", "/"]
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
            exit(0)
        elif sys.argv[2] == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
            exit(0)
        elif sys.argv[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
            exit(0)
        elif sys.argv[2] == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
            exit(0)
