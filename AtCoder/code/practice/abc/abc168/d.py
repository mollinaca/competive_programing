#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,M = map(int,input().split())

f = True 
R = {} # 通路
D = {} # 深さ
S = {} # 道標
for i in range(1,N+1):
    R[i] = []
    D[i] = N+1
    if i == 1:
        pass
    else:
        S[i] = None

for _ in range(M):
    a,b = map(int,input().split())
    R[a].append(b)
    R[b].append(a)

# 部屋の深さを調べる
from collections import deque
q = deque()
start = (1,0)
D[1] = 0
q.append(start)


while q:
    x,d = q.popleft()
    nx = x+1
    if N < nx:
        pass
    else:
        if D[nx] == N+1: # 未探索
            # 隣接する最も浅い部屋の深さ
            t = N+1
            for r in R[nx]:
                t = min(t,D[r])
            D[nx] = t+1
            pos = (nx,t+1)
            q.append(pos)
        else:
            pass

D2 = sorted(D.items(), key=lambda x:x[1])
L = [] # 1と道標でつながった部屋
# 道標を置く
for r,d in D2:
    ok = False

    if r == 1:
        continue

    # 深さ1 → 部屋1と隣接
    if d == 1:
        S[r] = 1
        L.append(r)
        continue

    # 深さ2以上
    for x in L:
        if x in R[r]:
            S[r] = x
            L.append(r)
            ok = True

    for x in R[r]:
        if x in L:
            S[r] = x
            L.append(r)
            ok = True

    # どの部屋ともつながってないので達成できない
    if ok:
        continue
    else:
        f = False
        break

if f:
    print ("Yes")
    for ans in S.values():
        print (ans)

else:
    print ("No")
