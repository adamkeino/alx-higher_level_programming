#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        p = ''.join(map(str, my_list[:x]))
        print(p)
    except:
        pass
    m = 0
    for i in p:
        m += 1

    return (m)
