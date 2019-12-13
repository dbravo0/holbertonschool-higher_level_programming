#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    n1 = int(argv[1])
    n2 = int(argv[3])

    if argv[2] == '+':
        print("{} + {} = {}".format(n1, n2, add(n1, n2)))

    elif argv[2] == '-':
        print("{} - {} = {}".format(n1, n2, sub(n1, n2)))

    elif argv[2] == '*':
        print("{} * {} = {}".format(n1, n2, mul(n1, n2)))

    elif argv[2] == '/':
        print("{} / {} = {}".format(n1, n2, div(n1, n2)))

    elif argv[2] != '+' and '-' and '*' and '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
