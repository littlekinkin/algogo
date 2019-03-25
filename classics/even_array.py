#!/usr/bin/env python
# -*- coding:utf-8 -*-

#left even
#right odd
def is_odd(num):
    return num%2

def even1(arr):
    print('-'*10)
    print(arr)
    i = 0
    j = len(arr) - 1
    while(i<j):
        if is_odd(arr[j]):
            j -= 1
        elif not is_odd(arr[i]):
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
    return arr

def even2(arr):
    print('-'*10)
    print(arr)
    even_index = 0
    for index, num in enumerate(arr):
        if not is_odd(num):
            arr[index], arr[even_index] = arr[even_index], arr[index]
            even_index += 1
    return arr




for x in [[1,2,3,4,5], [1,3,3,4,6], [1,3,3,5,7], [2,4,6,8], [2,4,3,6,8]]:
    #print(even1(x))
    print(even2(x))

