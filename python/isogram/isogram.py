#!/usr/bin/env python

import string

def is_isogram(string_input):
    string_input = string_input.lower()

    flag = True

    for char in string_input:
        if char in string.ascii_lowercase and string_input.count(char) > 1:
            return False

    return flag
