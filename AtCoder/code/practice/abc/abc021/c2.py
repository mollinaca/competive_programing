#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
a,b = map(int,input().split())
M = int(input())

path = {} # 道路がつなぐ町の情報
path_r = {} # 町から町への距離、スタートの町(a)からの距離
z = [] # 探索済みの町
for i in range(1,N+1):
    path_r[i] = -1
for i in range(1,M+1):
    path[i] = []

for i in range(1,M+1):
    x,y = map(int,input().split())
    path[x].append(y)
    path[y].append(x)

from collections import deque
q = deque()
direction = [1,-1]

path_r[a] = 0
z.append(a)
q.append(a)

while q:
    p = q.popleft()
    for d in direction:
        np = p+d
        if 1 <= np <= N: # np は範囲内
            if np not in z: # 未探索
                tmp = float('inf') # np が隣接する最も近い町の距離を z からの全探索で求める

                for x in z: # x は探索済みの町
                    if x in path[np]: # np は探索済みの x と隣接する
                        tmp = min(tmp,path_r[x])

                path_r[np] = tmp + 1
                z.append(np)
                q.append(np)

            else: # 探索済み
                pass
        else: # 範囲外
            pass

path_r_sorted = sorted(path_r.items(), key=lambda x:x[1])

ans = 1
x = 0
count = 0
g_r = path_r[b]
for k,v in path_r_sorted:
    if v == g_r:
        ans *= count
        print (ans%1000000007)
        exit ()
    elif v == x:
        count += 1
    else:
        ans *= count
        x = v
        count = 1
