#!/usr/bin/env python3
# -*- coding: utf-8 -*-
H,W = map(int,input().split())
grid = [list(input()) for i in range(H)]
sy,sx,gy,gx = 0,0,0,0
direction = [[-1,0],[1,0],[0,-1],[0,1]]

for y,line in enumerate(grid):
    for x,p in enumerate(line):
        if grid[y][x] == "s":
            sx = x
            sy = y
        if grid[y][x] == "g":
            gx = x
            gy = y

start = (sy,sx)
from collections import deque
q = deque()
q.append(start)

while q:
    y,x = q.pop()
    for d in direction:
        ny = y+d[0]
        nx = x+d[1]

        if 0 <= ny < H and 0 <= nx < W:

            if grid[ny][nx] == ".":
                pos = (ny,nx)
                q.append(pos)
                grid[ny][nx] = "#"

            if ny == gy and nx == gx:
                # ゴールにたどり着いた
                print ("Yes")
                exit ()
        else:
            # 範囲外なので探索しない
            pass

# ゴールにたどり着けなかった
print ("No")
