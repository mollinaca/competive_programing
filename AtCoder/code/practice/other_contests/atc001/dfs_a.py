#!/usr/bin/env python3
# -*- coding: utf-8 -*-
H,W = map(int,input().split())
grid = [list(input()) for i in range(H)]

import sys
sys.setrecursionlimit(10**9)

def dfs (y,x):

    if  not ((0 <= y < H) and (0 <= x < W)):
        return

    if grid[y][x] == "#":
        return

    if grid[y][x] == "g":
        print ("Yes")
        exit ()

    grid[y][x] = "#"

    dfs (y,x+1)
    dfs (y,x-1)
    dfs (y+1,x)
    dfs (y-1,x)

    return

for y in range(H):
    for x in range(W):
        if grid[y][x] == "s":
            dfs (y,x)
            break

print ("No")
