#!/usr/bin/python3

def divisble_by_2(my_list=[]):
    multiples = []
    for idx in range(len(my_list)):
        if my_list[idx] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(false)

    return (multiples)
