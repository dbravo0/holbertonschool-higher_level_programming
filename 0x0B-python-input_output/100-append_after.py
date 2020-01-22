#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):

    result = ""
    with open(filename) as f:
        for line in f:
            result += line
            if search_string in line:
                result += new_string

    with open(filename, "w") as f:
        f.write(result)
