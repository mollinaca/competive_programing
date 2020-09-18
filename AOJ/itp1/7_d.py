#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m,l = map(int,input().split())
A = []
B = []

for _ in range(n):
    A.append(list(map(int,input().split())))
for _ in range(m):
    B.append(list(map(int,input().split())))

ans = []
for i in range(n):
    row = []
    for j in range(l):
        total = 0
        for k in range(m):
            total += A[i][k] * B[k][j]
        row.append(total)
    ans.append(row)

for line in ans:
    print(' '.join(map(str, line)))
