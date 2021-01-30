#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))
S = [0]
for i,a in enumerate(A):
    S.append(S[i]+a)

ans = 0
for s in set(S):
    c = S.count(s)
    if c == 0 or c == 1:
        pass
    else:
        ans += (c*(c-1))//2
print (ans)
