#!/usr/bin/python3


def print_uniq_combos():
    for a in range(10):
        for b in range(ai + 1, 10):
            if a == 8 and b == 9:
                print('{:d}{:d}'.format(a, b))
            else:
                print('{:d}{:d}'.format(a, b), end=', ')


if __name__ == '__main__':
    print_uniq_combos()
