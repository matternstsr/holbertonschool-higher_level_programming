#!/usr/bin/python3
def print_list_interger(my_list=[]):
    if type(my_list) == list and my_list is not None:
        for idx in my_list:
            print('{:d}'.format(idx))
