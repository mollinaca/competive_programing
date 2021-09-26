#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
from collections import deque
N = int(input())
A = deque(list(map(int,input().split())))

ANS = {}
for i in range(10):
    ANS[i] = 0

def op_f (q:deque) -> deque:
    x = q.popleft()
    y = q.popleft()
    q.appendleft((x+y)%10)
    return q

def op_g (q:deque) -> deque:
    x = q.popleft()
    y = q.popleft()
    q.appendleft((x*y)%10)
    return q

def dfs (q:deque):
    if len(q) == 1:
        ANS[q[0]] += 1
        return
    q_back = copy.deepcopy(q)
    dfs (op_f(q))
    q = copy.deepcopy(q_back)
    dfs (op_g(q))

dfs (A)

for a in ANS.values():
    print (a%998244353)
