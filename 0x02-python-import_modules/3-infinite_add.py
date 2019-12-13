#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    r = 0

    for i in argv[1:]:
        r += int(i)
    print("{:d}".format(r))
