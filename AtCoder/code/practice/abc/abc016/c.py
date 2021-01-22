#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,M = map(int,input().split())
F = {} # 友達関係
for i in range(1,N+1):
    F[i] = []

for _ in range(M):
    a,b = map(int,input().split())
    F[a].append(b)
    F[b].append(a)

for i in range(1,N+1):
    ans = 0
    l = []
    for x in F[i]:
        for y in F[x]:
            if y != i and y not in F[i] and y not in l:
                l.append(y)
                ans += 1
    print (ans)
