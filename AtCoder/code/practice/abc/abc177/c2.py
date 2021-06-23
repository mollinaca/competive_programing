#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))

ans = 0
for i,a1 in enumerate(A):
    for a2 in A[i+1::]:
        ans += a1*a2

print (ans%(10**9+7))
