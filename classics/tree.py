#!/usr/bin/env python
# -*- coding:utf-8 -*-

from queue import Queue

class Node():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pre_traverse(root):
    if not root:
        return
    print(root.value)
    pre_traverse(root.left)
    pre_traverse(root.right)

def pre_traverse4stack(root):
    if not root:
        return
    temp = []
    temp.append(root)
    while temp:
        now = temp.pop()
        print(now.value)
        if now.right:
            temp.append(now.right)
        if now.left:
            temp.append(now.left)


def mid_traverse(root):
    if not root:
        return
    mid_traverse(root.left)
    print(root.value)
    mid_traverse(root.right)

def post_traverse(root):
    if not root:
        return
    post_traverse(root.left)
    post_traverse(root.right)
    print(root.value)



'''
        D
      |   |  
    B       E
  |   |
A       C       G
            F
'''

if __name__ == '__main__':
    root = Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    pre_traverse(root)
    print('--')
    mid_traverse(root)
    print('--')
    post_traverse(root)
    print('--')
    pre_traverse4stack(root)


