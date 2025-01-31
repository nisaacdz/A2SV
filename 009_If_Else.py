#!/bin/python3

import math
import os
import random
import re
import sys

def categorize(n):
    if n % 2 == 1 or 6 >= n <= 20:
        return "Weird"
    else:
        return "Not Weird"

if __name__ == '__main__':
    n = int(input().strip())
    print(categorize(n))
