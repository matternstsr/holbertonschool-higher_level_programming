#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is not None and type(roman_string) == str:
        romdandict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }


