#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    result = 0
    length = len(sys.argv) - 1
    if length == 0:
        print("0")
    for i in range(1, length + 1):
        result += int(sys.argv[i])
    print("{}".format(result))
