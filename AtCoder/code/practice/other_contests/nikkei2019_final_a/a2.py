#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
L = list(map(int,input().split()))
W = [0]
for i,x in enumerate(L):
    W.append(L[i]+W[i])

for i in range(1,N+1):
    ans = 0
    for j in range(len(W)-i):
        t = W[j+i] - W[j]
        if ans < t:
            ans = t
    
    print (ans)
