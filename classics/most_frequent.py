#!/usr/bin/env python
# -*- coding:utf-8 -*-


def find_most_common(digit_str):
    res = [0]*10
    for d in digit_str:
        d = int(d)
        res[d] += 1
    num = 0
    c = 0
    for index, v in enumerate(res):
        if v >= c:
            num = index
            c = v
    print(num)

def remove_space(i_str):
    newc = ''
    for w in i_str:
        if w is not ' ':
            newc += w
    print(newc)

def second_large(i_str):
    res = [0]* 1201
    for w in i_str.split():
        w = int(w)
        res[w] += 1
    c = 0
    max_n = 0
    for index in range(1200,0,-1):
        if res[index]:
            c+= 1
            max_n = index
        if c is 2:
            break
    print(index)





for _ in range(int(input())):
    _ = input()
    i_str = input()
    second_large(i_str)


