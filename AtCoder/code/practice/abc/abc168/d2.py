#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,M = map(int,input().split())

R = {} # 通路
Rd = {} # 部屋ごとの深さ 
S = {} # 道標
for i in range(1,N+1):
    R[i] = []
    Rd[i] = N+1 # N+1で初期化する
    if i == 1:
        pass
    else:
        S[i] = None

Dr = {} # 深さごとの部屋
for i in range(M):
    if i == 0:
        Dr[i] = [1]
    else:
        Dr[i] = [] # 深さは最大でN

for _ in range(M):
    a,b = map(int,input().split())
    R[a].append(b)
    R[b].append(a)

# 部屋の深さを調べる
from collections import deque
q = deque()

L = [1] # 調査済みの部屋
start = (1,0)
Rd[1] = 0
q.append(start)
while q:
    x,d = q.popleft()
    for nx in R[x]:
        if nx not in L:
            if N < nx:
                pass
            else:
                # 隣接する最も浅い部屋の深さ
                t = N+1
                for r in R[nx]:
                    t = min(t,Rd[r])
                t += 1
                Rd[nx] = t
                Dr[t].append(nx)
                pos = (nx,t)
                q.append(pos)
                L.append(nx)

# 道標を置く
for d,v in Dr.items():
    for r in v:
        ok = False

        if r == 1: # 部屋1
            continue

        # 深さ1 → 部屋1と隣接
        if d == 1:
            S[r] = 1
            continue

        # 深さd(d<1)以上 -> 深さ d-1 の部屋と隣接
        for x in Dr[d-1]:
            if x in R[r]:
                S[r] = x
                ok = True
                break

        if not ok:
            print ("No")
            exit ()

print ("Yes")
for v in S.values():
    print (v)
