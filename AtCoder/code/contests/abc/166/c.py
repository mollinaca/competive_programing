#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
H = list(map(int,input().split()))
T = {}

for i in range(1,n+1):
    T[i] = "good"

for _ in range(m):
    a,b = map(int,input().split())
    if H[a-1] <= H[b-1]:
        T[a] = "bad"
    if H[a-1] >= H[b-1]:
        T[b] = "bad"

#print (T)
print (list(T.values()).count("good"))
