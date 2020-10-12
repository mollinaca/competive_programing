#!/usr/bin/env python3
# -*- coding: utf-8 -*-
h,w = map(int,input().split())
grid = [list(input()) for i in range(h)]
ans = 0

for i in range(h):
    for j in range(w):
        if grid[i][j] == "." and j+1 < w and grid[i][j+1] == ".":
            ans += 1
        if grid[i][j] == "." and i+1 < h and grid[i+1][j] == ".":
            ans += 1

print (ans)
