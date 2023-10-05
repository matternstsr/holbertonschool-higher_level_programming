#!/usr/bin/python3
# 1-my_list.py
# Matthew Ernst 6628@holbertonstudents.com
""" inheritance """


class MyList(list):
    """implemention of a sorted print for list class"""

    def print_sorted(self):
        """Prints a list in an order"""
        print(sorted(self))
