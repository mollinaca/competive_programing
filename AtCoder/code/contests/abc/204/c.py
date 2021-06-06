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

R2 = {}
for k,v in R.items():
    q1 = deque(v) # 調査用 queue
    q2 = []       # 調査済み list
    r = []        # 到達可能都市 list
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
                    q1.appendleft (y)
                    r.append (y)
    R2[k] = r

ans = 0
for l in R2.values():
    ans += len(l)
print (ans)
