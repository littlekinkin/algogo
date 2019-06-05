#!/usr/bin/env python
# -*- coding:utf-8 -*-

from queue import Queue

#breadth-first: queue
#depth-first: stack, recursive

class Node():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.layer = None

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

def layer_traverse(root):
    q = Queue()
    q.put(root)
    while not q.empty():
        now = q.get()
        print(now.value)
        if now.left:
            q.put(now.left)
        if now.right:
            q.put(now.right)

def right_node(root):
    q = Queue()
    q.put(root)
    root.layer = 1
    result = []
    while not q.empty():
        now = q.get()
        result.append((now.value, now.layer))
        if now.left:
            now.left.layer = now.layer + 1
            q.put(now.left)
        if now.right:
            now.right.layer = now.layer + 1
            q.put(now.right)
    print(result)
    for index, x in enumerate(result):
        if index == 0 or index == len(result) -1:
            print(x[0])
        if index > 0 and index < len(result)-1 and x[1] != result[index+1][1]:
            print(x[0])


    


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
    print('--')
    layer_traverse(root)
    print('--')
    right_node(root)


