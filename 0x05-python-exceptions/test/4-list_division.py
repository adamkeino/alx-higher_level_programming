#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quo = []
    for i in range(list_length):
        try:
            quo.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            quo.append(0)
            continue
        except(TypeError, ValueError):
            print("wrong type")
            quo.append(0)
            continue
        except:
            print("out of range")
            quo.append(0)
            continue
        finally:
            pass
    return quo
