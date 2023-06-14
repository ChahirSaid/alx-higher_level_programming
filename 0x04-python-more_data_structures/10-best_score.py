#!/usr/bin/python3
def best_score(a_dictionary):
    key = None
    biggestNumber = 0

    if not a_dictionary:
        return key
    for k in a_dictionary:
        if a_dictionary[k] > biggestNumber:
            biggestNumber = a_dictionary[k]
            key = k
    return key
