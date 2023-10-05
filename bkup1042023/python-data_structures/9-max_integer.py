#!/usr/bin/python3


def max_integer(my_list=[]):
    max_value = 0
    if len(my_list) == 0:
        return None
    for index, element in enumerate(my_list):
        if index == 0 or element > max_value:
            max_value = element
    return max_value
