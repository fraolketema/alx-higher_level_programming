#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    number = 0
    denn = 0
    for tuples in my_list:
        number += tuples[0] * tuples[1]
        denn += tuples[1]
    return (number / denn)
