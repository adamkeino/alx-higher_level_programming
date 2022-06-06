#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 0:
        temp = list(tuple_b)
        temp.append(0)
        temp.append(0)
        tuple_b = tuple(temp)
    elif len(tuple_b) == 1:
        temp = list(tuple_b)
        temp.append(0)
        tuple_b = tuple(temp)
    elif len(tuple_a) == 0:
        temp = list(tuple_a)
        temp.append(0)
        temp.append(0)
        tuple_a = tuple(temp)
    elif len(tuple_a) == 1:
        temp = list(tuple_a)
        temp.append(0)
        tuple_a = tuple(temp)
    
    sum_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return sum_tuple
