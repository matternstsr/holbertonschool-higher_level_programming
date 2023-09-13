#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        created = dict(a_dictionary)
        for key, value in created.items():
            created[key] = value * 2
            return created
