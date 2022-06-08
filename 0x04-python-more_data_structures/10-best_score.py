#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for key, val in a_dictionary.items():
            if max(val):
                return key
