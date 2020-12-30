#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

WA = [0]
WB = [0]
for a in A:
    WA.append(WA[-1]+a)

for b in B:
    WB.append(WB[-1]+b)

ans, j = 0, M
for i in range(N+1):
    if WA[i] > K:
        break

    while WB[j] + WA[i] > K:
        j -= 1
    ans = max(ans,i+j)

print (ans)
