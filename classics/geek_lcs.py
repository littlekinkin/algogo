#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

def lcs(l1, l2, lookup):
    k  = (len(l1), len(l2))
    if not len(l1) or not len(l2):
        lookup[k] = 0
    if k not in lookup:
        if l1[-1] == l2[-1]:
            lookup[k] = lcs(l1[:-1], l2[:-1], lookup) + 1
        else:
            lookup[k] = max(lcs(l1, l2[:-1], lookup), lcs(l1[:-1], l2, lookup))
    return lookup[k]



case_num = int(sys.stdin.readline().strip())
for i in range(case_num):
    lookup = {}
    _ = sys.stdin.readline().strip()
    l1 = sys.stdin.readline().strip()
    l2 = sys.stdin.readline().strip()
    print(lcs(l1, l2, lookup))
    
