#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is not None:
        new_list = []
        for idx, value in enumerate(my_list):
            if my_list[i] == search:
                new_list.append(replace)
            else:
                new_list.append(my_list[idx])
        return new_list
