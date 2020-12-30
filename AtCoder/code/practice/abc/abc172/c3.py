#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

sumAt = [0]
sumBt = [0]
for a in A:
    sumAt.append(sumAt[-1]+a)
for b in B:
    sumBt.append(sumBt[-1]+b)
WA = sumAt
WB = sumBt[1::]

ans = 0
import bisect
for ai,a in enumerate(WA):
    if K < a:
        break

    t = K-a
    bi = bisect.bisect_right(WB,t)
    if ans < ai+bi:
        ans = ai+bi

print (ans)
