#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,K = map(int,input().split())
T = []
for _ in range(N):
    T.append(list(map(int,input().split())))

l = []
for i in range(K):
    for _ in range(N):
        l.append(i)

d = []

from itertools import permutations
for x in permutations(l,N):
    if x in d:
        continue
    p = 0
    for i,v in enumerate(x):
        p ^= T[i][v]
    
    d.append(x)

    if p == 0:
        print ("Found")
        exit ()

print ("Nothing")
