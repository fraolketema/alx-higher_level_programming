#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        count_len = 0
        for x in range(x):
            print("{}".format(my_list[x]), end="")
            count_len += 1
        print()
        return count_len
    except IndexError:
        print()
        return count_len
