#!/usr/bin/env python
# -*- coding:utf-8 -*-

#https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps/0/?ref=self

from collections import defaultdict

def jump_count(ll):
    if not ll[0]:
        return -1
    lookup = [0]* len(ll)
    for index, num in enumerate(ll):
        if  not num:
            continue
        for step in range(0, num+1):
            reach = step + index
            if reach >= len(ll):
                continue
            if lookup[reach]:
                lookup[reach] = min(lookup[index]+1, lookup[reach])
            else:
                lookup[reach] = lookup[index] + 1
    return lookup[len(ll) - 1] if lookup[len(ll) - 1] else -1

def jump_count2(ll):
    reach_dict = {0:0}
    index_steps = dict(enumerate(ll))
    #tt = [ll[0]]
    res = [0]
    for index in res:
        for step in range(1, index_steps[index] + 1):
            reach = index + step
            if reach > len(ll) -1:
                continue
            if reach in reach_dict and reach_dict[index] > reach_dict[reach]:
                continue
            reach_dict[reach] = min(reach_dict[index] + 1, reach_dict[reach]) if reach in reach_dict  else reach_dict[index] + 1
            res.append(reach)
    return reach_dict.get(len(ll)-1, -1)

def jump_count3(arr):
    size = len(arr)
    count = 0
    reach = arr[0]
    index = 0
    while reach < size:
        old_reach = reach
        for step in range(index, reach):
            if reach >= size-1:
                return count+1
            else:
                reach_new = step + arr[step]
            if reach_new > reach:
                reach = reach_new
        index = old_reach
        count += 1
    return count









for i in range(int(input())):
    input()
    ll = [int(x) for x in input().split()]
    print(jump_count3(ll))
