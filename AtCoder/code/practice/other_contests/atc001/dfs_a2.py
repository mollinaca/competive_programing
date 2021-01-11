#!/usr/bin/env python3
# -*- coding: utf-8 -*-
H,W = map(int,input().split())
grid = [list(input()) for i in range(H)]
tansakuzumi = [[-1]*W for i in range(H)]
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

start = (sy,sx,0)
from collections import deque
q = deque()
q.append(start)

while q:
    y,x,r = q.popleft()
    for d in direction:
        ny = y+d[0]
        nx = x+d[1]

        if 0 <= ny < H and 0 <= nx < W:

            if tansakuzumi[ny][nx] == -1:
                if grid[ny][nx] == ".":
                    # 未探索の道
                    pos = (ny,nx,r+1)
                    q.append(pos)
                    tansakuzumi[ny][nx] = r+1
                else:
                    # 未探索の壁
                    tansakuzumi[ny][nx] = 0
            else:
                # 探索済み
                pass

            if ny == gy and nx == gx:
                # ゴールにたどり着いた
                #print ("Yes",r+1)
                print ("Yes")
                exit ()
        else:
            # 範囲外なので探索しない
            pass

# ゴールにたどり着けなかった
print ("No")
