#!/usr/bin/python3
new_str = ""
for i in range(122, 96, -1):
    if i % 2 != 0:
        new_str += chr(i - 32)
    else:
        new_str += chr(i)
print("{}".format(new_str), end="")
