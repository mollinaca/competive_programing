#!/usr/bin/env python3
# -*- coding: utf-8 -*-
k,s = map(int,input().split())
ans = 0
for a in range(k+1):
    for b in range(k+1):
        c = s - (a+b)
        if 0 <= c <= k:
            ans += 1
print (ans)
