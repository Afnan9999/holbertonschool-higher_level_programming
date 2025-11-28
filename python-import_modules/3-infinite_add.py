#!/usr/bin/python3
"""Print the sum of all command-line arguments"""

import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # exclude script name
    total = 0

    for arg in args:
        total += int(arg)

    print(total)
