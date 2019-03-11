#!/usr/bin/env python
# -*- coding:utf-8 -*-

#https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps/0/?ref=self

from collections import defaultdict

def jump_count(ll):
    ret = 0
    last = 0
    curr = 0
    for i in range(len(ll)):
        if i > last:
            last = curr
            ret += 1
        curr = max(curr, i+ll[i])
    return ret

for i in range(int(input())):
    input()
    ll = [int(x) for x in input().split()]
    print(jump_count(ll))
