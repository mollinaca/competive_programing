#!/usr/bin/env python3
# -*- coding: utf-8 -*-
H,W,K = map(int,input().split())
grid = [list(input()) for i in range(H)]
ans = 0

X = H+W
for i in range(2**X):
    B = [0]*X
    for j in range(X):
        if ((i>>j)&1):
            B[X-1-j] = 1

    k = 0
    for y,line in enumerate(grid):
        for x,p in enumerate(line):
            if B[y] == 1 or B[x+H] == 1:
                pass
                #print ("X",end="")
            else:
                #print (grid[y][x],end="")
                if grid[y][x] == "#":
                    k += 1
        #print () # 改行
    if k == K:
        ans += 1

print (ans)
