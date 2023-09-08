#!/usr/bin/python3


def print_list_integer(my_list=[]):
    if type(my_list) == list and my_list is not None:
        for n in my_list:
            print('{:d}'.format(n))
