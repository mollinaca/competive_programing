#!/usr/bin/env python3
# -*- coding: utf-8 -*-
K = int(input())

from collections import deque
q = deque()

for i in range(1,10):
    q.append(i)

for _ in range(K-1):
    x = q.popleft()
    if x%10 != 0:
        q.append(10*x + x%10 - 1)
    q.append(10*x + (x%10))
    if x%10 != 9:
        q.append(10*x + x%10 + 1)

ans = q.popleft()
print (ans)
