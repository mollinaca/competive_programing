#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque
N,M = map(int,input().split())
R = {}
for i in range (1,N+1):
    R[i] = [i]
for _ in range (M):
    A,B = map(int,input().split())
    R[A].append(B)

ans = 0
for k,v in R.items():
    q1 = deque(v) # 調査用 queue
    q2 = []       # 調査済み list
    if k == 1:
        r = []        # 到達可能都市 list
    else:
        for k2 in range(1,k):
            for r2 in R[k2]:
                if r2 not in 
    while True:
        if not q1:
            break
        x = q1.popleft ()
        if x in q2:
            continue
        else:
            q2.append (x)
            for y in R[x]:
                if y not in r:
                    r.append (y)
                    if y not in q1:
                        q1.appendleft (y)
                    ans += 1
print (ans)
