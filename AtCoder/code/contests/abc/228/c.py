#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,K = map(int,input().split())
P = {}
for i in range(1,N+1):
    l = list(map(int,input().split()))
    P[i] = sum(l)
P2 = sorted(P.items(), key=lambda x:x[1], reverse=True)
x = P2[K-1][1]

for v in P.values():
    if x-v <= 300:
        print ("Yes")
    else:
        print ("No")
