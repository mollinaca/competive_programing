#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
T = sorted(list(map(int,input().split())))
ans = 10**18

for i in range(2**N):
    L = [0]*N
    s0 = 0
    s1 = 0
    for j in range(N):
        if ((i>>j)&1):
            L[N-1-j] = 1

    for l,t in zip (L,T):
        if l == 0:
            s0 += t
        else:
            s1 += t
    ans = min(ans,max(s0,s1))

print (ans)
