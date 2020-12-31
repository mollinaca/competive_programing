#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))

ta1 = [0]
ta2 = [0]
for i in range(N):
    ta1.append(ta1[-1]+A1[i])
    ta2.append(ta2[-1]+A2[-(i+1)])

sumA1 = ta1[1::]
sumA2 = ta2[1::]
sumA2.reverse()

ans = 0
for a1,a2 in zip(sumA1,sumA2):
    ans = max(ans,a1+a2)
print (ans)
