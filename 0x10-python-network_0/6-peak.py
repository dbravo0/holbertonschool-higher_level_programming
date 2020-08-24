#!/usr/bin/python3
def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    else:
        ls = len(list_of_integers)
        list_of_integers.sort()
        full_ls = list_of_integers[ls-1]
    return (full_ls)
