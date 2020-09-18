#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
R = []
ans = -(float('inf'))

for i in range(n):
    r = int(input())
    if i == 0:
        min_r = r
        continue
    else:
        ans = max(ans,r-min_r)
        if r < min_r: min_r = r

print (ans)
