#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    for elem in range(x):
        try:
            print("{:d}".format(my_list[elem]), end='')
            cont += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            raise
    print("")
    return cont
