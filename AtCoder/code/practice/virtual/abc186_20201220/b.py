#!/usr/bin/env python3
# -*- coding: utf-8 -*-
h,w = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(h)]
m = float('inf')

for line in grid:
    for block in line:
        if block < m:
            m = block

ans = 0
for line in grid:
    for block in line:
        ans += (block - m)

print (ans)
