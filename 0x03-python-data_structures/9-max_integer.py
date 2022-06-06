#!/usr/bin/python3
def max_integer(my_list=[]):
    ans = 0
    if len(my_list) == 0:
        return None
    else:
        for i in range(0, (len(my_list)-1)):
            if my_list[i] > ans:
                ans = my_list[i]
        return ans

