#!/usr/bin/env python

import string

def is_pangram(sentence):
    sentence = sentence.lower()

    for ch in string.ascii_lowercase:
        if ch not in sentence:
            return False

    return True
