#!/usr/bin/env python3
# -*- coding: utf-8 -*-
D,G = map(int,input().split())
ans = float('inf')

d = {}
for i in range(1,D+1):
    p,c = map(int,input().split())
    d[i] = (p,c,(100*i*p)+c)

print (d)

n = D
for i in range(2**n):
    L = [0]*n
    for j in range(n):
        if ((i>>j)&1):
            L[n-1-j] = 1

    # 処理
    print (i,L)
    score = 0
    for l in range(n):
        if L[l] == 1:
            score += d[l+1][2]
        
    print (score)

