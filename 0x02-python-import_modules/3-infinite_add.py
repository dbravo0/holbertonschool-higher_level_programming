#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    a = len(argv) -1
    r = 0

    for i in range(a):
        r += int(argv[i + 1])
    print(r)
