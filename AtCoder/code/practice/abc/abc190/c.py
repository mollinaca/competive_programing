#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,M = map(int,input().split())
A = []
B = []
for _ in range(M):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

K = int(input())
D = {}
for i in range(K):
    c,d = map(int,input().split())
    D[i] = [c,d]

ans = 0
for i in range(2**K):
    L = [0]*K
    for j in range(K):
        if ((i>>j)&1):
            L[K-1-j] = 1

    bd = [] # ボールがおいてある皿
    for x,l in enumerate(L):
        bd.append(D[x][l])

    # 満たされる条件の数
    t = 0
    for a,b in zip(A,B):
        if a in bd and b in bd:
            t += 1
    ans = max(ans,t)

print (ans)
