#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers, a and b"""
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
