#!/usr/bin/python3

def remove_char_at(string_input, n):
    copy = ""
    for i in range(len(string_input)):
        if i == n:
            continue
        copy += string_input[i]
    return copy
