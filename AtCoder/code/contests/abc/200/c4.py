#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))

A2 = []
for a in A:
    A2.append(a%200)

A3 = set(A2)
A4 = {}
for a in A3:
    if a not in A4:
        A4[a] = A2.count(a)
    else:
        pass

ans = 0
for a in A4.values():
    ans += a*(a-1)//2

print (ans)
