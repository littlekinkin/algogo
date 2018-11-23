#!/usr/bin/env python
# -*- coding:utf-8 -*-

#https://practice.geeksforgeeks.org/problems/subset-sum-problem/0/?ref=self
def sss(ll):
    ss = sum(ll)
    if ss%2:
        return 'NO'
    half = int(ss/2)
    dp = [int(not x) for x in range(half + 1)]
    for c in ll:
        for x in range(half, c-1, -1):
            dp[x] |= dp[x - c]
    return 'YES' if dp[half] else 'NO'

for i in range(int(input())):
    input()
    ll = [int(x) for x in input().split()]
    print(sss(ll))
