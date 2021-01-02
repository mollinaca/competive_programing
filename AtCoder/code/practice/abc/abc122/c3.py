#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,Q = map(int,input().split())
S = input()

s = [0]
for i in range(1,len(S)):
    if S[i-1]+S[i] == "AC":
        s.append(s[i-1]+1)
    else:
        s.append(s[i-1])

for _ in range(Q):
    l,r = map(int,input().split())
    print (s[r-1]-s[l-1])
