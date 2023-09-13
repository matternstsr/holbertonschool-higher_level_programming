#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    cnt = 0
    for idx in range(x):
        try:
            print('{}'.format(my_list[idx]), end='')
            cnt += 1
        except (ValueError, TypeError):
            pass
    print()
    return cnt
