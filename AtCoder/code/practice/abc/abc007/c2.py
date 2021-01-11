#!/usr/bin/env python3
# -*- coding: utf-8 -*-
R,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
grid = [list(input()) for i in range(R)]
sy -= 1
sx -= 1
gy -= 1
gx -= 1

tansakuzumi = [[0]*C for i in range(R)]
direction = [[-1,0],[1,0],[0,-1],[0,1]]

from collections import deque
q = deque()
start = (sy,sx,0)
q.append(start)
tansakuzumi[sx][sy] = 1

while q:
    y,x,d = q.popleft()
    for i in direction:
        ny = y+i[0]
        nx = x+i[1]
        if tansakuzumi[ny][nx] == 0: # 未探索
            if grid[ny][nx] == ".": # 道（壁ではない）
                pos = (ny,nx,d+1)
                q.append(pos)
                tansakuzumi[ny][nx] = d+1
            else: # 未探索で壁だった
                tansakuzumi[ny][nx] = d+1
        else: # 探索済みだった
            pass

        if ny == gy and nx == gx:
            print (d+1)
            exit ()
