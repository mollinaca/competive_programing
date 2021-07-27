#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bf(graph:list, start:int, goal:int):
    # graph : 隣接リスト
    # start : 求めたい始点
    # goal  : 求めたい終点

    n = len(graph) # ノード数
    cost = [float('inf')] * n # 各ノードまでのコスト
    cost[start] = 0 # 始点のコストを0にする

    f = True # 終了flag
    while f:
        f = False
        for i,node_list in enumerate(graph):
            for g,w in node_list:
                if cost[i] + w < cost[g]:
                    cost[g] = cost[i] + w
                    f = True

        # Todo:
        # 負の閉路があるかどうかチェック

#   return cost[goal] # 求めたいのが特定ノードまでの距離であればこちらでOK
    return cost

def main ():
    # 隣接リストの取得、頂点数N、辺の数M
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
#   s, g = map(int, input().split())

    print (graph)
    print (bf(graph, 0, 1)) # ここで, 終点として入力されている 1 は実質意味をなしていない

if __name__ == '__main__':
  main()