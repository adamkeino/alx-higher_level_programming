#!/usr/bin/python3
def multiple_returns(sentence):
    m = tuple(sentence)
    return (len(m), m[0] if len(sentence) > 0 else None)
