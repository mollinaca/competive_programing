#!/usr/bin/env python3
# -*- coding: utf-8 -*-
H,W = map(int,input().split())
grid = [list(input()) for i in range(H)]

pcount = 0
for line in grid:
    for p in line:
        if p == ".":
            pcount += 1

direction = [[-1,0],[1,0],[0,-1],[0,1]]
from collections import deque
q = deque()
ans = 0

for y,line in enumerate(grid):
    for x,p in enumerate(line):
        grid_z = [[-1]*W for i in range(H)]

        if p == ".":
            # 初期化
            sy,sx = y,x
            start = [sy,sx,0]
            q.append(start)
            grid_z[sy][sx] = 0

            # 各マスへの距離を調査
            while q:
                qy,qx,qd = q.popleft()
                for d in direction:
                    ny = qy + d[0]
                    nx = qx + d[1]
                    nd = qd + 1

                    if 0 <= ny < H and 0 <= nx < W: # 範囲内
                        if grid_z[ny][nx] != -1: # 探索済み
                            continue
                        else:
                            if grid[ny][nx] == "#": # 壁
                                grid_z[ny][nx] = -2
                                continue
                            else: # 道
                                grid_z[ny][nx] = nd
                                pos = [ny,nx,nd]
                                q.append(pos)
                    else: # 範囲外
                        pass
        else: # 壁
            pass

        for lz in grid_z:
            for p in lz:
                ans = max(ans,p)

print (ans)
