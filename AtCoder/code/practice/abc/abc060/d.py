#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,W = map(int,input().split())
w = []
v = []
for i in range(1,N+1):
    a,b = map(int,input().split()) 
    w.append(a)
    v.append(b)

ans = 0
for i in range(2**N):
    l = [0]*N
    for j in range(N):
        if ((i>>j)&1):
            l[N-1-j] = 1

    wt = 0
    for x,y in zip(l,w):
        wt += x*y

    if W < wt:
        continue
    else:
        vt = 0
        for x,y in zip(l,v):
            vt += x*y
        
        ans = max(ans,vt)

print (ans)
