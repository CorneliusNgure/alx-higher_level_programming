#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """print only the x elements of my_list

       Args:
            my_list (list) => The list
            x (int) => The number of elements.

        Return:
            The number of items printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return (count)
