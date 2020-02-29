import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING expression as parameter.
#

def is_operator(operator):
    if operator in '+-':
        return True
    return False

def prefix_to_infix(pre_exp):
    
    stack = list()
    for item in list(pre_exp)[::-1]:
        if is_operator(item):
            op1 = stack.pop()
            op2 = stack.pop()
            temp = f'({op1}{item}{op2})'
            stack.append(temp)
            
        else:
            stack.append(item)
    return stack

def solve(expression):
    return prefix_to_infix(expression)


print(solve('-1-21'))