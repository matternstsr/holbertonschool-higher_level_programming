#!/usr/bin/python3
def print_list_inteerger(my_list=[]):
    if type(my_list) == list and my list is not None:
        for idx in my_list:
            print('{:d}'.format(idx))
