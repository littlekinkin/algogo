#!/usr/bin/env python
# -*- coding:utf-8 -*-
#https://practice.geeksforgeeks.org/problems/coin-change/0/?ref=self
import sys
import copy


def cc(total, coins):
    coins = sorted(coins)
    re = [[x] for x in coins]
    dc = {}
    for x in coins:
        dc[x] = 1
    for x in re:
        for c in coins:
            tsum = sum(x) + c
            if x[-1] < c or tsum > total:
                continue
            newc = x + [c]
            re.append(newc)
            dc[tsum] = dc.get(tsum, 0) + 1
    return dc.get(total, 0)


def cc2(total, coins):
    rr = set()
    re = [[x] for x in coins]
    for x in re:
        for c in coins:
            if sum(x) + c <= total:
                newc = x + [c]
                if sum(newc) == total:
                    newc = tuple(sorted(newc))
                    rr.add(newc)
                    continue
                if newc not in re:
                    re.append(newc)
    print(rr)
    return len(rr)

def cc3(total, coins):
    dp = [int(not i) for i in range(total + 1)]
    for c in coins:
        for j in range(c, total + 1):
            dp[j] += dp[j - c]
    print(dp[-1])



case_num = int(sys.stdin.readline().strip())
for i in range(case_num):
    _ = sys.stdin.readline().strip()
    coins = [int(x) for x in sys.stdin.readline().strip().split()]
    total = int(sys.stdin.readline().strip())
    print(cc2(total, coins))
    print(cc(total, coins))
    print(cc3(total, coins))
