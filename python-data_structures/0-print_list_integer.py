#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if type(my_list) == list and len(my_list) > 0:
        for idx in my_list:
            print('{:d}'.format(idx))
