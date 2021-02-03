#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))
ans = 0

for l in range(N):
    for r in range(l+1,N+1):
        x = min(A[l:r])
        if ans < x*(r-l+1):
            ans = x*(r-l)

print (ans)
