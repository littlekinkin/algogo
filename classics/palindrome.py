#!/usr/bin/env python
import sys

def is_palindrome(input_str):
    input_str = input_str.lower()
    left = 0
    right = len(input_str) - 1
    while left < right:
        if not input_str[left].strip():
            left += 1
        elif not input_str[right].strip():
            right -= 1
        elif input_str[left] != input_str[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

print(is_palindrome(sys.argv[1]))
