#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,W = map(int,input().split())
d = {}
for _ in range(N):
    s,t,p = map(int,input().split())
    for i in range(s,t):
        if i not in d:
            d[i] = p
        else:
            d[i] += p

        if W < d[i]:
            print ("No")
            exit ()

print ("Yes")
