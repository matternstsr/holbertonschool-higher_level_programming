#!/usr/bin/python3


def max_integer(my_list=[]):
    max_int = 0
    if len(my_list) == 0:
        return None
    for index, element in enumerate(my_list):
        if index == 0 or element > max_int:
            max_int = element
    return max_int
