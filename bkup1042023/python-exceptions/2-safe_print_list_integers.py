#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    cnt = 0
    for idx in range(x):
        try:
            print('{:d}'.format(my_list[idx]), end='')
            cnt += 1
        except ValueError:
            pass
        except TypeError:
            pass

    print()
    return cnt
