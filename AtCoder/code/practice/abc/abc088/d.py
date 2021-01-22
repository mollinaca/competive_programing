#!/usr/bin/env python3
# -*- coding: utf-8 -*-
H,W = map(int,input().split())
grid = [list(input()) for i in range(H)]

# 黒マスの数
black = 0
for line in grid:
    for p in line:
        if p == "#":
            black += 1

direction = [[-1,0],[1,0],[0,-1],[0,1]]
grid_z = [[-1]*W for i in range(H)] # -1:未探索, -2:黒, n:そこまでの距離
start = [0,0,0] # [y,x,d]
grid_z[0][0] = 0

from collections import deque
q = deque()
q.append(start)
goal = False
while q:
    y,x,dist = q.popleft()
    for d in direction:
        ny = y+d[0]
        nx = x+d[1]
        nd = dist+1

        if 0 <= ny < H and 0 <= nx < W: # 範囲内
            if grid_z[ny][nx] == -1: # 未探索
                if grid[ny][nx] == "#": # 黒
                    grid_z[ny][nx] = -2
                else: # 白
                    grid_z[ny][nx] = nd
                    pos = [ny,nx,nd]
                    q.append(pos)
                    if ny == H-1 and nx == W-1: # ゴールに到達
                        goal = True
                        break
            else: # 探索済み
                pass
        else: # 範囲外
            pass

    if goal:
        break

if goal:
    print ((H*W)-(grid_z[H-1][W-1]+1+black))
else:
    print (-1)
