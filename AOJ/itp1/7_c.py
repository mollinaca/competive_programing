#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r,c = map(int,input().split())
x = [] * r

for _ in range(r):
    l = list(map(int,input().split()))
    l.append(sum(l))
    x.append (l)

l = []
for i in range(c+1):
    total = 0
    for j in range(r):
        total += x[j][i]
    l.append (total)
x.append (l)

for l in x:
    print(' '.join(map(str, l)))
