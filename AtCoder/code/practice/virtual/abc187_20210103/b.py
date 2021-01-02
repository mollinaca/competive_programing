#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
pos = []
for _ in range(N):
    x,y = map(int,input().split())
    pos.append((x,y))

ans = 0
import itertools
for p1,p2 in itertools.combinations(pos,2):
    if -1 <= (p2[1]-p1[1])/(p2[0]-p1[0]) <= 1:
        ans += 1

print (ans)
