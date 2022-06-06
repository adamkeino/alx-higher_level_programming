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
    elif len(tuple_a) >= 2:
        temp_a = list(tuple_a)
        temp_a = temp_a[0:2]
        tuple_a = tuple(temp_a)
    elif len(tuple_b) >= 2:
        temp_b = list(tuple_b)
        temp_b = temp_b[0:2]
        tuple_b = tuple(temp_b)
    
    sum_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return sum_tuple
