#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,K = map(int,input().split())
A = list(map(int,input().split()))

W = [0]
for i,a in enumerate(A):
    W.append(W[i]+a)

ans = 0
for i in range(N-K+1):
    ans += W[i+K] - W[i]

print (ans)
