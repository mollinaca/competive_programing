#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,D,H = map(int,input().split())
k = 10**18
for _ in range(N):
    d,h = map(int,input().split())
    k = min(k,(H-h)/(D-d))
print (max(0,H-D*k))
