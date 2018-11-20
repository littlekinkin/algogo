#!/usr/bin/env python
# -*- coding:utf-8 -*-
#https://practice.geeksforgeeks.org/problems/coin-change/0/?ref=self
import sys

def cc(total, coins):
    re = [[total]]
    for tmp in re:
        rest = tmp[-1]
        for c in coins:
            t = tmp[:]
            tc = rest - c
            if tc >= 0:
                t.append(tc)
                re.append(t)
    for x in re:
        for i in range(len(x)):



case_num = int(sys.stdin.readline().strip())
for i in range(case_num):
    _ = sys.stdin.readline().strip()
    coins = [int(x) for x in sys.stdin.readline().strip().split()]
    total = int(sys.stdin.readline().strip())
    cc(total, coins)
    
