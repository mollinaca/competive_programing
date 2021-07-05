#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def adj_list ():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)  # 有向グラフなら消す
    print(graph)

def adj_list_weight ():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))  # 有向グラフなら消す
    print(graph)  # [[2, 3], [3, 1], [5, 9]], ..., [...]]

def adj_mtx ():
    n, m = map(int, input().split())
    graph = [[0]*n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1
#        graph[b-1][a-1] = 1  # 有向グラフなら消す
    print(graph)  # [[0, 1, 1, 0, 1], ..., [1, 0, 1, 1, 0]]

def adj_mtx_weight ():
    n, m = map(int, input().split())
    graph = [[0]*n for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u-1][v-1] = w
        graph[v-1][u-1] = w  # 有向グラフなら消す
    print(graph)  # [[0, 2, 3, 0, 1], ..., [2, 0, 3, 0, 0]

adj_mtx_weight ()
#adj_list_weight ()

