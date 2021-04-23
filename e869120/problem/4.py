#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://twitter.com/e869120/status/1377752658149175299/photo/2
H,W = map(int,input().split())
grid = []
ans = []
for _ in range(H):
    grid.append(list(map(int,input().split())))
    ans.append([0]*W)

R = []
C = []
for w in range(W):
    x = 0
    for h in range(H):
        x += grid[h][w]
    R.append(x)
for h in range(H):
    x = 0
    for w in range(W):
        x += grid[h][w]
    C.append(x)

for h in range(H):
    for w in range(W):
        ans[h][w] = R[w] + C[h] - grid[h][w]

for l in ans:
    print(' '.join(map(str, l)))
