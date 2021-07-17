#!/usr/bin/env python3
# -*- coding: utf-8 -*-
H,W,C = map(int,input().split())
grid = []
for h in range(1,H+1):
    l = list(map(int,input().split()))
    for w,a in enumerate(l):
        grid.append((h,w+1,a))

# 全探索
ans = 10**18
for i,v in enumerate(grid):
    for j in range(i+1,H*W):
        x = grid[i][2] + grid[j][2]
        y = C * (abs(grid[i][0]-grid[j][0])+abs(grid[i][1]-grid[j][1]))
        ans = min (ans,x+y)

print (ans)
