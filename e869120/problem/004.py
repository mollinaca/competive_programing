#!/usr/bin/env python3
# -*- coding: utf-8 -*-
H,W = map(int,input().split())
h = []
w = [0]*W
A = []
for _ in range(H):
    A2 = list(map(int,input().split()))
    A.append(A2)
    h.append(sum(A2))
    for i,a2 in enumerate(A2):
        w[i] += a2
 
for i,line in enumerate(A):
    for j,p in enumerate(line):
        print (h[i]+w[j]-p,end=" ")
    print ()