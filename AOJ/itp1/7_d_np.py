#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
n,m,l = map(int,input().split())
A = []
B = []

for _ in range(n):
    A.append(list(map(int,input().split())))
A = np.matrix(A)
for _ in range(m):
    B.append(list(map(int,input().split())))
B = np.matrix(B)

ans = np.dot(A,B)
for l in ans.tolist():
    print(' '.join(map(str, l)))
