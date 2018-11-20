#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

def lis(arr):
    ll= len(arr)
    re = [1] * ll
    for i in range(ll):
        for j in range(i):
            if arr[i] > arr[j] and re[i] < re[j] + 1:
                re[i] = re[j] + 1
    return max(re)

case_num = int(sys.stdin.readline().strip())
for i in range(case_num):
    length = sys.stdin.readline().strip()
    inputs = sys.stdin.readline().strip()
    inputs = [int(x) for x in inputs.split()]
    print(lis(inputs))


