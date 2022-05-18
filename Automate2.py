#!/usr/bin/env python

import json


def contains_ip(line: str):
    if type(line) is not str:
        return
    dots = line.count('.')
    return dots > 0 and dots % 3 == 0 and len(line) <= 15


def is_jsonable(string: str):
    try:
        json.loads(string)
    except ValueError:
        return False
    return True


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        print(x)
        # If the Nested key-value
        # pair is of dict type
        if type(x) is dict:

            for a in x:
                flatten(x[a], name + a + '_')

        # If the Nested key-value
        # pair is of list type
        elif type(x) is list:

            i = 0

            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


# opening and reading the file
with open('detail.txt', encoding='utf-8') as fh:
    string = fh.readlines()

# initializing the list objects
valid = []

def add_to_list(a):
    if contains_ip(a):
        valid.append(a)

# extracting the IP addresses
for line in string:
    line = line.strip().replace('\n,', '')
    arr = line.split(':', 1)  # split into key, value array
    if len(arr) > 1 and is_jsonable(arr[1].strip()): # check if value is json obj
        obj = flatten_json(json.loads(arr[1].strip())) # flatten json obj
        for v in obj.values(): # iterate values to check ip address
            add_to_list(v)
    else:  # ip addresses
        for a in arr:
            add_to_list(a.strip())
print(valid, len(valid))      