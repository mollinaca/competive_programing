#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))
P = {}
for i in range(1,(2**N)+1):
    P[A[i-1]] = i

for _ in range(N-1):
    tmp = []
    for i in range(0,len(A)-1,2):
        tmp.append(max(A[i],A[i+1]))
    A = tmp

print (P[min(A)])
