#!/usr/bin/python3
"""
Function that constructs the pascal triangle
"""


def pascal_triangle(n):
    la = []
    for i in range(n):
        la.append(''.join(map(str, str(11**i))))
    
    return (la)
