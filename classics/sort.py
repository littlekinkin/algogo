#!/usr/bin/env python
# -*- coding:utf-8 -*-

def q(arr, low, high):
    if low < high:
        k_index = partion(arr, low, high)
        q(arr, low, k_index-1)
        q(arr, k_index+1, high)

def partion(arr, low, high):
    left, right = low, high

    k = arr[left]

    while left < right:
        while arr[right] > k:
            right -= 1
        while arr[left] <= k:
            left += 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low] = arr[right]
    arr[right] = k
    return right


a = [2,3,4,5,1,7]
q(a, 0, len(a)-1)
print(a)

