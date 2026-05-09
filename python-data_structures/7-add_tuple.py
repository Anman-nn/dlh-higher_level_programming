#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)[:2]
    list_b = list(tuple_b)[:2]
    if len(list_a)<2:
        list_a.append(0)
    if len(list_b)<2:
        list_b.append(0)
    return tuple(map(sum, zip(list_a, list_b)))
