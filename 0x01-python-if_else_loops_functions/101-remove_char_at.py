#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    j = str[0:n]
    j += str[n+1:]
    return j
