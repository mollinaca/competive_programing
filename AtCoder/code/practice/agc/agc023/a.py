#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))

ans = 0
for i in range(N):
    for j in range(i+1,N+1):
        if sum(A[i:j]) == 0:
            ans += 1
print (ans)
