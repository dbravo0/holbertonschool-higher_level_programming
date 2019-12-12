#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    l = len(argv)
    r = 0

    for i in range(1, l):
        r += int(argv[i])
    print(r)

