#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
L = []
R = []
for _ in range(m):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)

print (max(0,min(R)-max(L)+1))
