#!/usr/bin/env python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
       return True
   except:
    print("Exception: {}".format(e), file=sys.stderr)
    return False
