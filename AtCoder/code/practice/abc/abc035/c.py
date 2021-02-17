#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,Q = map(int,input().split())
X = [0]*N
for _ in range(Q):
    l,r = map(int,input().split())
    for x in range(l-1,r):
        X[x] += 1

for x in X:
    if x%2 == 0:
        print (0,end="")
    else:
        print (1,end="")
print ()
