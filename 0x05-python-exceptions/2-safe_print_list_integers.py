#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers.
       Args:
            my_list(list) => the list argument.
            x(int)        => the no. of items on the list to be printed.
        Return:
            No. of ints printed.
    """

    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (count)
