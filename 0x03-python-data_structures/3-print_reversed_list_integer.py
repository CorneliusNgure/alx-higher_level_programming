#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 0:
        reversed_list = my_list[::-1]
        for item in reversed_list:
            print("{:d}".format(item))
