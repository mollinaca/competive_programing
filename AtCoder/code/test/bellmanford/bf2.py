#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bf(s,n,es):
    # s:始点, n:頂点数, es: es[i]-> [辺の始点、辺の終点、辺のコスト]

    d = [float("inf")]*n # 重みの初期化
    d[s] = 0

    # 最短路を計算する
    for _ in range(n-1):
        # es: 辺 i について
        for p,q,r in es:
            if d[p] != float("inf") and d[p] + r < d[q]:
                d[q] = d[p] + r # 更新
                print ("始点:",p,"終点:",q,"コスト:",r,"コスト更新:",d[q])

    # 負の閉路がないかチェック
    for _ in range(n-1):
        # es: 辺 i について
        for p,q,r in es:
            #更新される点は負閉路の影響を受けるので-infを入れる
            if d[q] > d[p] + r:
                d[q] = -float("inf")

    return d


n,w = map(int,input().split()) #n:頂点数　w:辺の数
es = [] # es[i]: [辺の始点,辺の終点,辺のコスト] 隣接リスト
for _ in range(w):
    x,y,z = map(int,input().split())
    es.append([x,y,z])

print(bf(0,n,es))
