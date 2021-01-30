#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))
S = [0]
for i,a in enumerate(A):
    S.append(S[i]+a)
S.sort()

ans = 0
ps = 0
c = 0
for i,s in enumerate(S):
    if i == 0:
        ps = s
        c = 1
    elif i == N:
        if s == ps:
            c += 1
        ans += (c*(c-1))//2
    else:
        if s == ps:
            c += 1
        else:
            ans += (c*(c-1))//2
            ps = s
            c = 1

print (ans)
