#!/usr/bin/env python3
# -*- coding: utf-8 -*-
H,W,D = map(int,input().split())
G = {}
for y in range(H):
    l = list(map(int,input().split()))
    for x,i in enumerate(l):
        G[i] = (y+1,x+1)

Q = int(input())
for _ in range(Q):
    L,R = map(int,input().split())
    if L == R:
        print (0)
        continue

    for i in range(L,R+1,D):
        print (i,G[i])
        # わからん、累積和でどうにかするらしい
