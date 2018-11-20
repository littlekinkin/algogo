#!/usr/bin/env python
# -*- coding:utf-8 -*-
#https://practice.geeksforgeeks.org/problems/coin-change/0/?ref=self
import sys

def cc(total, coins, alls):
    if total == 0:
        return 0
    for c in coins:
        rest = total - c
        if rest < 0:
            continue


    pass

case_num = int(sys.stdin.readline().strip())
for i in range(case_num):
    _ = sys.stdin.readline().strip()
    coins = [int(x) for x in sys.stdin.readline().strip().split()]
    total = int(sys.stdin.readline().strip())
    
