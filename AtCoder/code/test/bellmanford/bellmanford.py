#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 頂点数N、経路数Mの重み付き無向グラフが入力される
n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u-1][v-1] = w
    graph[v-1][u-1] = w

print(graph)

def bellman_ford(graph, num_node):
    cost = [float('inf') for i in range(num_node)]
    cost[0] = 0

    while True:
        for v in graph:
            s = v[0]
            g = v[1]
            c = v[2]
            print (v)
            print (s,g,c)
            if cost[s] + c < cost[g]:
                cost[g] = cost[s] + c
            else:
                break
    
    return cost

print (bellman_ford(graph,n))
