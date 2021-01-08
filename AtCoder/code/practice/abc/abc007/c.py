#!/usr/bin/env python3
# -*- coding: utf-8 -*-
R,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
sy -= 1
sx -= 1
gy -= 1
gx -= 1

grid = [input() for i in range(R)]
tmp_grid = [[-1] * C for i in range(R)]

from collections import deque
q = deque()
q.append((sx,sy,0))
tmp_grid[sy][sx] == 0
d = [[1,0],[-1,0],[0,1],[0,-1]]

while q:
    y,x,tmp = q.popleft()
    for i in d:
        ny = y+i[0]
        nx = x+i[1]
        if grid[ny][nx] == '.' and tmp_grid[ny][nx] == -1: # 未探索で道なら
            tmp_grid[ny][nx] = tmp+1 # 経路への歩数を+１
            q.append((ny,nx,tmp+1)) # キューに積む

print (tmp_grid[gy][gx])
