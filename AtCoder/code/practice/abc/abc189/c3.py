#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))
ans = 0
x = float('inf')

for l in range(N):
    x = A[l]
    for r in range(l,N):
        x = min(x,A[r])
        if ans < x*(r-l+1):
            ans = x*(r-l+1)
print (ans)
