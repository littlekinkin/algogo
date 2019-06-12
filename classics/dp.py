#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time


#coin
def t1():
    cc = [1, 3, 5]
    tt = 11
    mm = {}
    mm[0] = 0
    for i in range(1, tt + 1):
        if i not in mm:
            mm[i] = 100
        for index, co in enumerate(cc):
            if co <= i and mm[i - co] + 1 < mm[i]:
                mm[i] = mm[i-co] + 1
    return mm[tt]

'''
Like Divide and Conquer, Dynamic Programming combines solutions to sub-problems.
Dynamic Programming is mainly used when solutions of same subproblems are needed again and again.
In dynamic programming, computed solutions to subproblems are stored in a table so that these don’t have to be recomputed.
So Dynamic Programming is not useful when there are no common (overlapping) subproblems because there is no point storing the solutions if they are not needed again
'''
def fib(n):
    if n <=1:
        return n
    return fib(n-1) + fib(n-2)
'''
                         fib(5)
                     /             \
               fib(4)                fib(3)
             /      \                /     \
         fib(3)      fib(2)         fib(2)    fib(1)
        /     \        /    \       /    \
  fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
  /    \
fib(1) fib(0)
'''

#Memoization (Top Down)
def fib_top2down(n, lookup):
    if n <= 1:
        lookup[n] = n
    if n not in lookup:
        lookup[n] = fib_top2down(n-1, lookup) + fib_top2down(n-2, lookup)
    return lookup[n]

#Tabulation (Bottom Up)
def fib_b2u(n):
    ff = {}
    ff[0] = 0
    ff[1] = 1
    for i in range(2, n+1):
        ff[i] = ff[i-1] + ff[i-2]
    return ff[n]
'''
Overlapping Subproblems
Optimal Substructure
Optimal Substructure: 
A given problems has Optimal Substructure Property if optimal solution of the given problem can be obtained by using optimal solutions of its subproblems
'''

'''
Longest Increasing Subsequence
'''
def lis(arr):
    max_len = 0
    n = len(arr)
    lis = [1]*n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis)

def max_sub(arr):
    pass

def lcs(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0
    if s1[-1] == s2[-1]:
        return 1 + lcs(s1[:-1], s2[:-1])
    else:
        return max([lcs(s1, s2[:-1]), lcs(s1[:-1], s2)])


def comp_fib():
    count = 20
    a = {}
    start = time.time()
    for i in range(100):
        fib(count)
    print 'recursive take:', time.time() - start
    start = time.time()
    for i in range(count):
        fib_top2down(count, a)
    print 'topdown take:', time.time() - start
    start = time.time()
    for i in range(count):
        fib_b2u(count)
    print 'b2u take:', time.time() - start




if __name__ == '__main__':
    print t1()
    a = {}
    k = 10
    print fib(k)
    print fib_top2down(k, a)
    print fib_b2u(k)
    print lis([10, 22, 9, 33, 21, 50, 41, 60])
    print lcs('1234', '1423')
    comp_fib()

