#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    dent = 0

    for tupe in my_list:
        number += tupe[0] * tupe[1]
        dent += tupe[1]

    return (number / dent)
