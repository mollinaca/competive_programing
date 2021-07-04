#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque
import itertools

N,M = map(int,input().split())
P = {}
for i in range(1,N+1):
    P[i] = {}

for _ in range(M):
    a,b,c = map(int,input().split())
    d = P[a]
    d[b] = c
    P[a] = d

def f (s,t,k) -> int:
    if s == t:
        return 0

    q = deque() # 探索用キュー
    start = s
    goal = t
    z = {s:0} # 探索済み管理用辞書 key:探索済み都市 value:その都市までの移動コスト
    c = 0 # 初期移動コスト
    q.append(s)

    # bfs
    while q:
        np = q.popleft()
        dP = P[np]
        for x,y in dP.items():
            c = z[np]
            if x == t: # ゴールにたどり着いた
                c += y
                return c
            else: # ゴールにたどりつかなかった
                if x <= k: # 探索対象都市なら
                    q.append(x) # 次の探索対象としてキューに積む
                    c += y
                    if x in z:
                        z[x] = min(c,z[x]) # 既に記録されている移動コストより短い移動コストで移動できるなら上書きする
                    else:
                        z[x] = c # 対象の場所までの移動コストを記録する
                else: # x は k より大きい都市なので探索対象外
                    pass

    # ゴールにたどり着けなかった
    return 0

l = [i for i in range(1,N+1)]
ans = 0
for s in l:
    for t in l:
        for k in l:
            a = f(s,t,k)
            ans += a

print (ans)
