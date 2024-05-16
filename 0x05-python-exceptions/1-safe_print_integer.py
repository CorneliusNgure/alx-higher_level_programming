def safe_print_integer(value):
    """ prints an integer with "{:d}".format().

        Args:
            value(int) - The value to be printed.

        Return:
            True: if value correctly printed.
            False: otherwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
