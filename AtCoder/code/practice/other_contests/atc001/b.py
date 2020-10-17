#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,q = map(int,input().split())

g = {}
for i in range(1,n+1):
    g[i] = []

for _ in range(q):
    print (g)
    p,a,b = map(int,input().split())

    if p == 0: # 連結クエリ
        if a not in g[b]:
            g[b].append(a)
            g[a].append(b)

    else: # 判定クエリ
        if b in g[a]:
            print ('Yes')
        else:
            print ('No')

# できてない