#!/usr/bin/python3

def multiple_returns(sentence):
    lent = len(sentence)

    if lent != 0:
        return (lent, sentence[0])
    else:
        return (lent, None)
