#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,K = map(int,input().split())
ans = 0

l = []
for _ in range(N):
    l.append(list(map(int,input().split())))

c = [i for i in range(1,N)]

import itertools
for v in itertools.permutations(c):
    path = [0]
    for k in v:
        path.append(k)
    path.append(0)

    cost = 0
    for i in range(len(path)-1):
        cost += l[path[i]][path[i+1]]

    if cost == K:
        ans += 1

print (ans)
