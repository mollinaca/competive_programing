#!/usr/bin/env python3
# -*- coding: utf-8 -*-
h,w = map(int,input().split())
grid = [[int(s) for s in list(input())] for i in range(h)]

def grid_c1(grid,n):
    ret = []
    for line in grid:
        ret.append(line[n])

    return ret
    
def grid_st(grid):
    ret = []
    sr,er = 0,len(grid)-1
    sc,ec = 0,len(grid[0])-1

    while sr <= er and sc <= ec:
        for col in range(sc,ec+1):
            ret.append(grid[sr][col])

        for row in range(sr+1,er+1):
            ret.append(grid[row][ec])

        for col in reversed(range(sc,ec)):
            ret.append(grid[er][col])

        for row in reversed(range(sr+1,er)):
            ret.append(grid[row][sr])

        sr += 1 
        er -= 1
        sc += 1
        ec -= 1

    return ret