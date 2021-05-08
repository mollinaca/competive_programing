#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque
N = int(input())
A = deque(map(int,input().split()))

ans = 0
while len(A) != 1:
    ai = A.popleft()
    A2 = deque()
    for a in A:
        t = ai - a
        if t%200 == 0:
            ans += 1
        A2.append(t)
    A = A2

print (ans)
