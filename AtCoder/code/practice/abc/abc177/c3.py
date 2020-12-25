#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))
W = [0]
for i,a in enumerate(A):
    W.append(W[i]+a)

ans = 0
for a,w in zip(A,W):
    ans += a*w

print (ans%(10**9+7))
