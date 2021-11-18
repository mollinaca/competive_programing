#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
L1 = [0]
L2 = [0]
for _ in range(N):
    C,P = map(int,input().split())
    if C == 1:
        L1.append(L1[-1]+P)
        L2.append(L2[-1])
    else: # C == 2
        L1.append(L1[-1])
        L2.append(L2[-1]+P)

Q = int(input())
for _ in range(Q):
    L,R = map(int,input().split())
    print (L1[R]-L1[L-1],L2[R]-L2[L-1])
