#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
l = []
r = 0 # 何個同じ色が連続しているか
for i in range(N):
    n = int(input())
    if i == 0:
        l.append(n)
        r += 1
    else:
        if i%2 == 0: # 奇数番目
            l.append(n)
            r += 1
        else: # 偶数番目
            if l[-1] == n:
                l.append(n)
                r += 1
            else:
                l = l[::-r] + [n]*r
                r = 0

    print (i,l)

print (l)
