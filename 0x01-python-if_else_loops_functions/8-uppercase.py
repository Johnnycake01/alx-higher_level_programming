#!/usr/bin/python3

def uppercase(strin):
    for c in strin:
        if 97 <= ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
