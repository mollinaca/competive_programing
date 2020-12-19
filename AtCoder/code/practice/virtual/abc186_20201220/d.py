#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = sorted(list(map(int,input().split())))

ans = 0
r = A[0]
for i in range(1,n):
    ans += i*A[i] - r
    r += A[i]

print (ans)
