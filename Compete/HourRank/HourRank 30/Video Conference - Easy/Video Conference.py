#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY names as parameter.
#

def solve(names):
    s = set()
    l = list()
    d = dict()
    for name in names:
        if name in d:
            d[name] += 1  
            l.append(name+ " "+str(d[name]))    
        else:
            d[name] = 1
            t = ""
            flag = False
            for i in range(len(name)):
                t += name[i:i+1]
                if t not in s and not flag:
                    flag = True
                    l.append(t)
                s.add(t)
            if not flag:
                l.append(name)
    return l
           



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    names = []

    for _ in range(n):
        names_item = input()
        names.append(names_item)

    res = solve(names)

    fptr.write('\n'.join(res))
    fptr.write('\n')

    fptr.close()
