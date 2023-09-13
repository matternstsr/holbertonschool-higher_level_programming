#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is not None:
        score = None
        person = None
        for key in a_dictionary.keys():
            if person None or a_dictionary[key] > person:
                person = a_dictionary[key]
                score = key
        return score
