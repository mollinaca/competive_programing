#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
t = []
for _ in range(n):
    t.append(int(input()))

ans = float('inf')
for i in range(2**n):
    l = [0]*n
    t0 = 0
    t1 = 0
    for j in range(n):
        if ((i>>j)&1):
            l[n-1-j] = 1

    for i,p in enumerate(l):
        if p == 0:
            t0 += t[i]
        else:
            t1 += t[i]

    if max(t0,t1) < ans:
        ans = max(t0,t1)

print (ans)
