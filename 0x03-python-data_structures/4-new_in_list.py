#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list == [] or idx < 0 or idx >= len(my_list):
        return my_list
    copy = my_list.copy()
    copy[idx] = element
    return copy
