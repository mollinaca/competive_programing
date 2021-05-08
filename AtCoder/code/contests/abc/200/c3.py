#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque
N = int(input())
A = list(map(int,input().split()))

D = {}
for a in A:
    aa = str(a)[-2::]
    if aa not in D:
        D[aa] = deque()
        D[aa].append(a)
    else:
        D[aa].append(a)

ans = 0
for A2 in D.values():
    if len(A2) < 2:
        pass
    else:
        while len(A2) != 1:
            ai = A2.popleft()
            A3 = deque()
            for a in A2:
                t = ai - a
                if t%200 == 0:
                    ans += 1
                A3.append(t)
            A2 = A3

print (ans)
