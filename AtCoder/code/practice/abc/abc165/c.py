#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,M,Q = map(int,input().split())
a,b,c,d = [],[],[],[]
ans = 0

for _ in range(Q):
    aa,bb,cc,dd = map(int,input().split())
    a.append(aa)
    b.append(bb)
    c.append(cc)
    d.append(dd)

# A を生成する
# 2 から M-1 までの N-2 個の組み合わせ
A = []
AA = [i for i in range(2,M)]
import itertools
for X in itertools.combinations(AA,N-2):
    Ax = [1]
    for x in X:
        Ax.append(x)
    Ax.append(M)
    A.append(Ax)

# 各 A から全探索
for Ax in A:
    At = 0
    for i in range(Q):
        if Ax[b[i]-1] - Ax[a[i]-1] == c[i]:
            At += d[i]
    ans = max(ans,At)

print (ans)
