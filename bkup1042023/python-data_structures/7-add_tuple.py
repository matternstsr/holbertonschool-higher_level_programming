#!/usr/bin/python3

def add_tuple(tuple1=(), tuple2=()):
    if len(tuple1) < 2:
        if len(tuple1) == 0:
            tuple1 = 0, 0
        else:
            tuple1 = tuple1[0], 0

    if len(tuple2) < 2:
        if len(tuple2) == 0:
            tuple2 = 0, 0
        else:
            tuple2 = tuple2[0], 0

    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])
