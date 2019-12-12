#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    c = len(argv) - 1
    r = 0

    for a in range(c):
        r += int(argv[a + 1])
    print(r)

