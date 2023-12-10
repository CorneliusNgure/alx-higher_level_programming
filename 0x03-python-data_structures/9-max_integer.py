#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    for x in my_list:
        if x >= my_list[x]:
            return x
        else:
            return my_list[x]
