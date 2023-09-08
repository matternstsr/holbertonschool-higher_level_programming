#!/usr/bin/python3


def print_list_interger(my_list=[]):
    if my_list is not None and type(my_list) == list:
        for idx in my_list:
            print("{:d}".format(idx))
