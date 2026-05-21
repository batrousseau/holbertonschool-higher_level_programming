#!/usr/bin/python3

__name__ = "__main__"

import sys

result: int = 0


for i in range(1, len(sys.argv)):
    result = result + int(sys.argv[i])

print("{}".format(result))
