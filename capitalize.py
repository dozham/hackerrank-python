#!/bin/python3

import math
import os
import random
import re
import sys
import string


# Complete the solve function below.
def solve(s):
    s = s.split(" ")
    return " ".join(i.capitalize() for i in s)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    s = 'hello Damn      WORLd'
    result = solve(s)

    print(result)
