#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        length = 0
        elem = None
    else:
        length = len(sentence)
        elem = sentence[0]
    return (length, elem)
