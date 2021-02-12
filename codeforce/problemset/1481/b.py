#!/usr/bin/env python3
# -*- coding: utf-8 -*-
t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    H = list(map(int,input().split()))
    M = {}
    for i in range(1,n+1):
        M[i] = H[i-1]

    m = 0
    for i in range(1,k+1): # i-th boulder
        # 転がる処理
        for m,h in M.items(): 
            if m == n: # 最後の山だったら止まらずにそのまま disposer にいく
                m = -1
                break

            if h >= M[m+1]:
                # 次の山へ転がる
                continue
            else:
                # この山で止まる
                M[m] += 1
                break

        if i == k:
            print (m)
