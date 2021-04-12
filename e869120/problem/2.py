#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())

for i in range(2**N):
    f = True
    L = [0]*N
    for j in range(N):
        if ((i>>j)&1):
            L[N-1-j] = 1

    # 処理
    if L.count(0) != L.count(1):
        continue

    x = 0
    for l in L:
        if l == 0:
            x += 1
        else:
            x -= 1
        if x < 0:
            f = False
            break

    if f:
        for l in L:
            if l == 0:
                print ('(',end='')
            else:
                print (')',end='')
        print ()
