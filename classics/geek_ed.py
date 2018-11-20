#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

def ed(l1, l2, lookup):
    k = (l1, l2)
    if not len(l1) or not len(l2):
        lookup[k] = max(len(l1), len(l2))
    if k not in lookup:
        if l1[-1] == l2[-1]:
            lookup[k] = ed(l1[:-1], l2[:-1], lookup)
        else:
            lookup[k] = min(ed(l1[:-1], l2, lookup), ed(l1, l2[:-1], lookup), ed(l1[:-1], l2[:-1], lookup)) + 1
    return lookup[k]


case_num = int(sys.stdin.readline().strip())
for i in range(case_num):
    lookup = {}
    _ = sys.stdin.readline().strip()
    l1 = sys.stdin.readline().strip()
    l1, l2 = l1.split()
    print(ed(l1, l2, lookup))
