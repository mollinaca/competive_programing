#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,K = map(int,input().split())
a = list(map(int,input().split()))

x = K//N
y = K%N

if y == 0:
    for i in range(N):
        print (x)
    exit ()

a2 = sorted(a)
ax = a2[y]
for i in range(N):
    if a[i] <ax:
        print (x+1)
    else:
        print (x)
