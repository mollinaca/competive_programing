#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,K = map(int,input().split())
C = list(map(int,input().split()))
m = len(set(C))

from collections import deque
q = deque(C[0:K])
ans = len(set(q))
for i in range(K,N):
    q.popleft()
    q.append(C[i])
    ans = max(ans, len(set(q)))
    if ans == m:
        print (ans)
        exit ()

print (ans)
