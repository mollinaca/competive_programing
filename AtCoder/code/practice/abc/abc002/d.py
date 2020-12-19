#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,M = map(int,input().split())
ans = 1
r = {}
for i in range(1,N+1):
    r[i] = []

for _ in range(M):
    x,y = map(int,input().split())
    r[x].append(y)
    r[y].append(x)
#print (r)

# 全パターンを作成
# 各パターンが成立条件を満たすか調べる
# 成立条件を満たすもののうち最大の人数のものが答え

# 全パターンを作成
for i in range(2**N):
    t = []
    for j in range(N):
        if ((i>>j)&1):
            t.append(j+1)

    # 処理
    #print (t)
    if len(t) <= 1:
        pass
    else:
        # 二人以上
        # 派閥として成立するか確認
        f = False
        for x,y in enumerate(t):
            for z in t[x+1::]:
                # yとzが知り合いでなければ終わり
                if not z in r[y]:
                    f = True
                    break
            if f:
                break
        if f:
            # 派閥として不成立
            continue
        else:
            # 派閥として成立
#            print ("成立:",t,len(t))
            if ans < len(t):
                ans = len(t)

print (ans)
