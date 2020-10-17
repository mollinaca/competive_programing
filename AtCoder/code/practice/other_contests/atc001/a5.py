#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/atc001/tasks/dfs_a
import sys
sys.setrecursionlimit(500000)

h,w = map(int,input().split())
grid = [list(input()) for i in range(h)]

def dfs(r,c):
#    print (r,c)

    if (not (0 <= c < w and 0 <= r < h)) or grid[r][c]=="#":
        return

    if grid[r][c]=="g":
        print("Yes")
        exit()

    grid[r][c]="#"
    dfs(r+1,c)
    dfs(r-1,c)
    dfs(r,c+1)
    dfs(r,c-1)

for i,y in enumerate(grid):
    if "s" in y:
        dfs(i, y.index("s"))
        break

print ('No')
