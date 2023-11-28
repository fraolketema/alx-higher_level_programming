#!/usr/bin/python3

def print_last_digit(number):
    ls = abs(number) % 10
    print(ls, end="")
    return ls
