#!/usr/bin/env python

import random
#洗牌算法
#Fisher–Yates shuffle

def fy_shuffle1(nums):
    for i in range(len(nums)-1, 0, -1):
        j = random.randint(0, i)
        nums[i], nums[j] = nums[j], nums[i]
    return nums

def fy_shuffle2(nums):
    for i in range(len(nums)-1):
        j = random.randint(i, len(nums)-1)
        nums[i], nums[j] = nums[j], nums[i]
    return nums
#正确性证明：每个元素在被shuffle之后出现在任意位置的概率都是1/N

#蓄水池采样
def reservoir_sample(in_arr, out_arr):
    topk = len(out_arr)
    for i in range(topk):
        out_arr[i] = in_arr[i]
    for i in range(topk, len(in_arr)):
        j = random.randint(0, i)
        if j < topk:
            out_arr[j] = in_arr[i]

#0采1次，1采2次，n-1采n次
#查表，限定指向的次数
def count_sample(n):
    table = {}
    index = 0
    for i in range(n):
        for j in range(i+1):
            table[index] = i
            index += 1
    i = random.randrange((1+n)*n/2)
    return table[i]

#构建坐标轴中的对角线，求和
def count_sample2(n):
    while True:
        i = random.randrange(n)
        j = random.randrange(n)
        if i+j < n:
            return i+j


