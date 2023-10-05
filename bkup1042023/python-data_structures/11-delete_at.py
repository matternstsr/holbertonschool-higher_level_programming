#!/usr/bin/python3

def delete_at(my_list=[], index=0):
    if index < 0 or index >= len(my_list):
        return my_list
    del my_list[index]
    return my_list
