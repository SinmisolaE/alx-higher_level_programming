#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("{:d} argument:".format(length))
    else:
        print("{:d} arguments:".format(length))
    for i in range(1, length + 1):
        print("{}: {}".format(i, sys.argv[i]))
