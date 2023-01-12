#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1: str, t2: str, date_fmt: str = "%a %d %b %Y %H:%M:%S %z") -> str:
    dt1, dt2 = (datetime.strptime(d, date_fmt) for d in (t1, t2))
    return str(int(abs((dt1 - dt2).total_seconds())))
    # return str(abs(int(dt1.timestamp() - dt2.timestamp())))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)
        # fptr.write(delta + '\n')

    # fptr.close()
