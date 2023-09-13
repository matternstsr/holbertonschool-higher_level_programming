#!/usr/bin/python3

def roman_to_int(roman_string):
    rom = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    num = 0
    val = 0
    nlen = roman_string

    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0
    for num in range(num, len(nlen)):
        if num < len(nlen) - 1 and rom[nlen[num]] < rom[nlen[num + 1]]:
            val -= rom[nlen[num]]
        else:
            val += rom[nlen[num]]
    return val
